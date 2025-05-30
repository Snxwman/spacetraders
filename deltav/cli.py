from typing import Any, Callable, cast
import traceback

from deltav.config import CONFIG
from deltav.defaults import Defaults
from deltav.spacetraders.agent import Agent
from deltav.spacetraders.api.response import SpaceTradersAPIResponse
from deltav.spacetraders.enums.faction import FactionSymbol
from deltav.spacetraders.enums.market import TradeSymbol
from deltav.spacetraders.game import SpaceTradersGame
from deltav.spacetraders.models.agent import AgentShape, RegisterAgentData
from deltav.spacetraders.api.client import SpaceTradersAPIClient
from deltav.spacetraders.models.contract import ContractDeliverShape
from deltav.spacetraders.models.market import CargoItemShape
from deltav.spacetraders.models.ship import ShipCargoInventoryShape, ShipCooldownShape
from deltav.spacetraders.models.waypoint import WaypointNavigateShape, WaypointShape
from deltav.spacetraders.ship import Ship
from deltav.spacetraders.contract import Contract
from deltav.spacetraders.enums.error import SpaceTradersAPIErrorCodes
from deltav.spacetraders.api.error import SpaceTradersAPIError

DEFAULT_FACTION = 'COSMIC'
active_agent: AgentShape | None = None


# def index_or_none(indexable, index: int) -> (Any | None):
#     try:
#         return indexable[index]
#     except IndexError:
#         return None
#
#
def get_next_command() -> list[str]:
    raw = input("cmd > ")
    return raw.split(' ')


# def get_prompt_answer(
#         prompt: str = '', 
#         answer = None, 
#         default = None, 
#         generate: Callable | None = None,  # pyright: ignore[reportMissingTypeArgument]
#         validate: Callable | None = None,  # pyright: ignore[reportMissingTypeArgument] 
#         allow_empty = False
#     ) -> str:
#
#     while (
#         answer is None or
#         answer == '' and allow_empty is False or
#         validate is not None and validate(answer) is False
#     ):
#         answer = input(prompt)
#
#     match answer:
#         case '{}' if generate is not None:
#             return generate()
#         case '-' if default is not None:
#             return default
#         case '' if allow_empty:
#             return answer
#         case _:
#             return answer
#
#
# def make_new_agent(args: list[str]):
#     callsign: str = ''
#     faction: str = ''
#
#
#     def generate_callsign() -> str:
#         return 'test_user'
#
#
#     def validate_callsign(callsign) -> bool:
#         return len(callsign) > 2 and len(callsign) < 15
#
#
#     def get_callsign(arg=None) -> str:
#         prompt = '[REQ] Enter agent\'s callsign: '
#         answer = get_prompt_answer(
#             prompt=prompt,
#             answer=arg, 
#             generate=generate_callsign, 
#             validate=validate_callsign
#         )
#         return answer.upper()
#
#
#     def get_faction(arg=None):
#         default = Defaults.FACTION.value
#         prompt = f'[OPT] Enter agent\'s faction (default: {default}): '
#         answer = get_prompt_answer(prompt=prompt, answer=arg, default=default)
#         return answer.upper()
#
#
#     # def get_email(arg=None):
#     #     prompt = '[OPT] Enter account email: '
#     #     answer = get_prompt_answer(prompt=prompt, answer=arg, default=CONFIG.email, allow_empty=True)
#     #     return answer
#
#
#     def confirm_agent_details() -> bool:
#         confirm = input('Confirm new agent details (y) or change value (callsign, faction): ')
#
#         match confirm:
#             case 'y':
#                 return True
#             case 'callsign':
#                 agent_data['symbol'] = get_callsign()
#             case 'faction':
#                 agent_data['faction'] = FactionSymbol[get_faction().upper()]
#             # case 'email':
#             #     agent_data['email'] = get_email()
#
#         return False
#
#     callsign = get_callsign(arg=index_or_none(args, 1)) 
#     faction = get_faction(arg=index_or_none(args, 2))
#
#     agent_data: RegisterAgentData = {
#         'symbol': callsign,
#         'faction': FactionSymbol[faction.upper()],
#     } 
#     
#     while confirm_agent_details() is not True:
#         print(agent_data)
#     
#     Agent.register(agent_data)
#
#
def usage():
    print('quit, contract, contracts, game, ships, help')


def accept_contract():
    print('Accepting contract...')
    # TODO: remove this placeholder
    temp_contract_id = 'cmb8cutehk6lxuo6x23gs1gu1'
    print(f'Available contract ID: {temp_contract_id}')
    contract_id = input('Enter contract ID to accept: ')

    contract = Contract.accept(contract_id)

    if isinstance(contract, SpaceTradersAPIError):
        print('You have already accepted the contract.')
    else:
        print(f'Contract {contract_id} accepted successfully.')

def get_contracts():
    # TODO: likely unneeded, as the game only allows for one contract at a time
    print('Getting contracts for active agent...')
    contracts = Contract.get_contracts()

    if not contracts:
        print('No contracts found.')
        return
    print('Available contracts:')
    print(contracts)


def get_contract(contract_id: str):
    print('Getting contracts for active agent...')
    contract = Contract.get_contract(contract_id)
    if not contract:
        print('No contracts found.')
        return
    print(f'Contract {contract_id} details:')
    print(contract)


def ships(active_agent: AgentShape | None):
    def navigate(shipSymbol: str, waypoint: WaypointNavigateShape):
        waypointSymbol = waypoint['waypointSymbol']
        print(f'Navigating ship {shipSymbol} to waypoint {waypointSymbol}...')
        try:
            Ship.navigate(shipSymbol, waypoint)
            print(f'Ship {shipSymbol} is now navigating to {waypointSymbol}.')
        except ValueError as e:
            print(f'Error navigating ship: {e}')


    def scanWaypoints(shipSymbol: str):
        print(f'Scanning waypoints for ship {shipSymbol}...')

        data = Ship.scan_waypoints(shipSymbol)
        if isinstance(data, SpaceTradersAPIError):
            print(f'Error scanning waypoints: {data}')
            return
        
        cooldown: ShipCooldownShape = cast(ShipCooldownShape, data['cooldown'])
        print(cooldown)
        waypoints: list[WaypointShape] = cast(list[WaypointShape], data['waypoints'])
        print(f'Waypoints for ship {shipSymbol}:')
        if isinstance(waypoints, list):
            for waypoint in waypoints:
                print(f'Location: {waypoint["symbol"]} ({waypoint["type"]}) at ({waypoint["x"]}, {waypoint["y"]})')
        else:
            print(waypoints)
            print(f'Error: Waypoints data is not in the expected format.')


    def getNavStatus(shipSymbol: str):
        print(f'Getting navigation status for ship {shipSymbol}...')
        status = Ship.get_nav_status(shipSymbol)
        if not status:
            print(f'No navigation status found for ship {shipSymbol}. (Error likely)')
            return
        print(f'Navigation status for ship {shipSymbol}:')
        print(status)


    def orbitShip(shipSymbol: str):
        print(f'Orbiting ship {shipSymbol}...')
        try:
            Ship.orbit_ship(shipSymbol)
            print(f'Ship {shipSymbol} is now orbiting.')
        except ValueError as e:
            print(f'Error orbiting ship: {e}')
    

    def dockShip(shipSymbol: str):
        print(f'Docking ship {shipSymbol}...')
        try:
            Ship.dock_ship(shipSymbol)
            print(f'Ship {shipSymbol} is now docked.')
        except ValueError as e:
            print(f'Error docking ship: {e}')


    def purchaseCargo(shipSymbol: str):
        cargoSymbol = input('Enter cargo symbol to purchase: ')
        units = int(input('Enter number of units to purchase: '))
        print(f'Purchasing {units} units of {cargoSymbol} for ship {shipSymbol}...')
        try:
            
            purchase: CargoItemShape = {
                'symbol': cargoSymbol,
                'units': units
            }
            Ship.purchase_cargo(shipSymbol, purchase)
            print(f'Purchased {units} units of {cargoSymbol} for ship {shipSymbol}.')
        except ValueError as e:
            print(f'Error purchasing cargo: {e}')


    def sellCargo(shipSymbol: str, tradeSymbol: str, units):
        print(f'Selling {units} units of {tradeSymbol} for ship {shipSymbol}...')
        try:
            sell: CargoItemShape = {
                'symbol': tradeSymbol,
                'units': units
            }
            data = Ship.sell_cargo(shipSymbol, sell)
            print(f'Sold {units} units of {tradeSymbol} for ship {shipSymbol}.')
        except ValueError as e:
            print(f'Error selling cargo: {e}')


    def viewCargo(shipSymbol: str):
        print(f'Viewing cargo for ship {shipSymbol}...')
        cargo = Ship.get_cargo(shipSymbol)
        if isinstance(cargo, SpaceTradersAPIError):
            print(f'Error getting cargo for ship {shipSymbol}: {cargo}')
            return
        print(f'Cargo for ship {shipSymbol}:')
        print(f'Cargo Hold: {cargo["units"]}/{cargo["capacity"]} units')
        inventory_data = cargo['inventory']
        if isinstance(inventory_data, list):
            inventory: ShipCargoInventoryShape = cast(ShipCargoInventoryShape, inventory_data)
            for item in inventory:
                item_casted = cast(CargoItemShape, item)
                print(f'{item_casted["symbol"]}: {item_casted["units"]} units')
        else:
            print("Error: Inventory data is not in the expected format.")
            

    def deliverCargo(shipSymbol: str):
        print(f'Delivering cargo for ship {shipSymbol}...')
        try:
            contract_id = input('Enter contract ID to deliver cargo for: ')
            tradeSymbol = input('Enter trade symbol: ').upper()
            units = int(input('Enter number of units to deliver: '))
            deliver: ContractDeliverShape = {
                'ship_symbol': shipSymbol,
                'trade_symbol': tradeSymbol,
                'units': units
            }
            delivery = Ship.deliver_contract(contract_id, deliver)
            print(f'Cargo delivered for ship {shipSymbol}:')
            print(delivery)
        except ValueError as e:
            print(f'Error delivering cargo: {e}')
    
    def extract_resources(shipSymbol: str):
        print(f'Extracting resources for ship {shipSymbol}...')
        extract = Ship.extract(shipSymbol)
        if isinstance(extract, SpaceTradersAPIError):
            print(f'Error extracting resources for ship {shipSymbol}: {extract}')
            return
        
        print(f'Resources extracted for ship {shipSymbol}:')
        print(f'Cargo Hold: {extract["cargo"]["units"]}/{extract["cargo"]["capacity"]} units')
        for item in extract['cargo']['inventory']:
            item_casted = cast(CargoItemShape, item)
            print(f'{item_casted["symbol"]}: {item_casted["units"]} units')
        print(f'Ship on cooldown for {extract["cooldown"]["remaining_seconds"]} seconds.')
        print(f'Ship {shipSymbol} has finished extracting resources.')

    def getCooldown(shipSymbol: str):
        print(f'Getting cooldowns for ship {shipSymbol}...')
        cooldown = Ship.get_cooldown(shipSymbol)
        if isinstance(cooldown, SpaceTradersAPIError):
            print(f'Error getting cooldown for ship {shipSymbol}: {cooldown}')
            print(f'Error code: {cooldown.code}')
            print(f'Probably means no cooldown?')
            return
        print(f'Cooldowns for ship {shipSymbol}:')
        print(f'Total Cooldown: {cooldown["total_seconds"]} seconds')
        print(f'Remaining: {cooldown["remaining_seconds"]} seconds')

    def jettisonCargo(shipSymbol: str, cargoSymbol: str, units):
        print(f'Jettisoning {units} units of {cargoSymbol} from ship {shipSymbol}...')
        try:
            jettison: CargoItemShape = {
                'symbol': cargoSymbol,
                'units': units
            }
            cargo_jettisoned = Ship.jettison_cargo(shipSymbol, jettison)
            print(f'Jettisoned {units} units of {cargoSymbol} from ship {shipSymbol}.')
        except ValueError as e:
            print(f'Error jettisoning cargo: {e}')
        

    print('Printing ships details...')
    
    current_ships = []
    if active_agent is not None:
        agent_instance = Agent(CONFIG.agent_token, active_agent)
        current_ships = Ship.my_ships()

    if not current_ships:
        if active_agent is not None:
            print(f'No ships found for agent {active_agent["symbol"]}.')
        else:
            print('No ships found because no active agent is set.')
        

    # print(f'Ships for {active_agent.callsign}:')
    if isinstance(current_ships, list):
        for x in range(len(current_ships)):
            ship = current_ships[x]
            print(f'#{x} + Ship Name: {ship['symbol']}\tLocation: {ship['nav']['waypointSymbol']}\tStatus: {ship['nav']['status']}\tCargo: {ship['cargo']['units']}/{ship['cargo']['capacity']} units')
    elif isinstance(current_ships, SpaceTradersAPIError):
        print(f'Error retrieving ships: {current_ships}')
        return
    else:
        print("Unexpected error: current_ships is not a list.")
        return
    
    # choose ship to do something with
    print('Select a ship by entering its index (0-based):')
    ship_chosen = int(input('Ship index: '))
    try:
        ship_index = ship_chosen
        if ship_index < 0 or ship_index >= len(current_ships):
            raise IndexError
        chosen_ship = current_ships[ship_index]
    
    except (IndexError, ValueError):
        print(f'Invalid ship index: {ship_chosen}. Please enter a valid index.')
        return
    
    def functions_on_orbit(shipSymbol: str):
        print('3. Dock Ship')
        print('4. Scan waypoints')
        print('5. Navigate to a waypoint')
        print('6. Extract Resources')
        print('7. View Cargo')

        action = input('Enter action number (1-9): ')
        match action:
            case '1':
                getNavStatus(shipSymbol)
            case '2':
                getCooldown(shipSymbol)
            case '3':
                dockShip(shipSymbol)
            case '4':
                print('Available waypoints:')
                scanWaypoints(shipSymbol)
            case '5':
                waypointSymbol = input('Enter waypoint symbol to navigate to: ').upper()
                waypoint: WaypointNavigateShape = {
                    'waypointSymbol': waypointSymbol
                }
                navigate(shipSymbol, waypoint)
                if not waypointSymbol:
                    print('No waypoint symbol provided. Aborting navigation.')
                    return
            case '6':
                extract_resources(shipSymbol)
            case '7':
                viewCargo(shipSymbol)
                
        
    def functions_while_docked(shipSymbol: str):
        print('3. Orbit Ship')
        print('4. View Cargo')
        print('5. Purchase Cargo')
        print('6. Sell Cargo')
        print('7. Deliver Cargo')
        print('8. Jettison Cargo')

        action = input('Enter action number (1-9): ')
        match action:
            case '1':
                getNavStatus(shipSymbol)
            case '2':
                getCooldown(shipSymbol)
            case '3':
                orbitShip(shipSymbol)
            case '4':
                viewCargo(shipSymbol)
            case '5':
                viewCargo(shipSymbol)
                purchaseCargo(shipSymbol)
            case '6':
                viewCargo(shipSymbol)
                cargo_symbol = input('Enter cargo symbol to sell: ')
                units = input('Enter number of units to sell: ')
                sellCargo(shipSymbol, cargo_symbol, units)
            case '7':
                # TODO: is this while docked or in orbit?
                deliverCargo(shipSymbol)
            case '8':
                viewCargo(shipSymbol)
                cargo_symbol = input('Enter cargo symbol to jettison: ')
                units = int(input('Enter number of units to jettison: '))
                jettisonCargo(shipSymbol, cargo_symbol, units)


    nav_status = chosen_ship['nav']['status']
    print(f'You selected ship: {chosen_ship["symbol"]} at {chosen_ship["nav"]["waypointSymbol"]}')
    print("What would you like to do with this ship?")
    print('1. Get Status of Ship')
    print('2. Get Cooldown of Ship')
    if nav_status == 'DOCKED':
        functions_while_docked(chosen_ship['symbol'])
    elif nav_status == 'IN_ORBIT':
        functions_on_orbit(chosen_ship['symbol'])


def run(client: SpaceTradersAPIClient):
    quit = False
    contract_id = 'cmb8cutehk6lxuo6x23gs1gu1'
    active_agent: AgentShape = {
        'symbol': 'AGENT_MOJO',
        'starting_faction': FactionSymbol.COSMIC,
        'headquarters': 'HQ',
        'credits': 1000,
        'ship_count': 1,
        'account_id': None
    }
    while not quit:
        args = list(filter(len, get_next_command()))

        match args[0]:
            case 'q' | 'quit' | 'e' | 'exit':
                quit = True
            case 'h' | 'help':
                usage()
            case 'game':
                from pprint import pp
                pp(SpaceTradersGame().fetch_server_status())
            # case 'new' | 'new-agent':
            #     make_new_agent(args)
            # case 'current' | 'agent' | 'me':
            #     get_current_agent()
            # TODO: negotate contract
            case 'contract' | 'contract' | 'c':
                get_contract(contract_id)
            case 'contracts':
                get_contracts()
            case 'accept' | 'a' | 'accept-contract':
                accept_contract()
            case 'ships' | 'ship' | 'my-ships' | 's':
                ships(active_agent)

