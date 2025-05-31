from spacetraders.api.enums import FactionSymbol
from spacetraders.config import CONFIG

from spacetraders.api.account import Account
from spacetraders.api.api import MAX_PAGE_LIMIT, SpaceTradersAPIRequest, SpaceTradersAPIResponse
from spacetraders.api.apierror import SpaceTradersAPIError
from spacetraders.api.data import RegisterAgentData
from spacetraders.api.response import AgentShape
from spacetraders.api.contract import Contract
from spacetraders.api.endpoints import SpaceTradersAPIEndpoint
from spacetraders.api.ship import Ship

from spacetraders.api.response import ShipShape, ShipRegistrationShape, ShipNavShape, ShipCrewShape, ShipFrameShape, ShipReactorShape, ShipEngineShape, ShipModulesShape, ShipMountsShape, ShipCargoShape, ShipFuelShape, ShipCooldownShape, ShipCargoInventoryShape
from spacetraders.api.response import ShipFuelConsumedShape, ShipRequirementsShape, ShipNavRouteShape, ShipNavRouteLocationShape, ShipRole
from spacetraders.api.enums import ShipMountDeposits
from datetime import datetime



class Agent:
    def __init__(self, token: str, agent_info: AgentShape) -> None:
        self.token: str = token

        if agent_info['account_id'] is not None:
            self.account: Account = Account(agent_info['account_id'])

        self.callsign: str = agent_info['symbol']
        self.credits: int = agent_info['credits']
        self.faction: FactionSymbol = agent_info['starting_faction']
        self.headquarters: str = agent_info['headquarters']
        self.ship_count: int = agent_info['ship_count']
        self.ships: list[ShipShape] = self.my_ships()
        self.contracts: list[Contract] = self.my_contracts()


    def save_to_file(self):
        ...
    

    def my_agent(self) -> AgentShape:
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.MY_AGENT) \
            .call()
        
        agent = res.spacetraders['data']['agent']
        return { 
            'account_id': agent['accountId'],
            'symbol': agent['symbol'],
            'headquarters': agent['headquarters'],
            'credits': agent['credits'],
            'starting_faction': FactionSymbol[agent['startingFaction']],
            'ship_count': agent['shipCount'],
        } 


    # TODO: move this to ship.py 
    @staticmethod
    def my_ships() -> list[ShipShape]:
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.MY_SHIPS) \
            .call()
        
        data = res.spacetraders['data']

        ships: list[ShipShape] = []
        for ship in data:
            registration: ShipRegistrationShape = {
                'name': ship['registration']['name'],
                'faction_symbol': FactionSymbol[ship['registration']['factionSymbol']],
                'role': ShipRole[ship['registration']['role']],
            }
            destination: ShipNavRouteLocationShape = {
                'symbol': ship['nav']['route']['destination']['symbol'],
                'type': ship['nav']['route']['destination']['type'],
                'system_symbol': ship['nav']['route']['destination']['symbol'],
                'x': ship['nav']['route']['destination']['x'],
                'y': ship['nav']['route']['destination']['y']
            }
            origin: ShipNavRouteLocationShape = {
                'symbol': ship['nav']['route']['origin']['symbol'],
                'type': ship['nav']['route']['origin']['type'],
                'system_symbol': ship['nav']['route']['origin']['symbol'],
                'x': ship['nav']['route']['origin']['x'],
                'y': ship['nav']['route']['origin']['y']
            }
            route: ShipNavRouteShape = {
                'destination': destination,
                'origin': origin,
                'departureTime': datetime.fromisoformat(ship['nav']['route']['departureTime']),
                'arrival': datetime.fromisoformat(ship['nav']['route']['arrival'])
            }
            nav: ShipNavShape = {
                'system_symbol': ship['nav']['systemSymbol'],
                'waypoint_symbol': ship['nav']['waypointSymbol'],
                'route': route,
                'status': ship['nav']['status'],
                'flightMode': ship['nav']['flightMode'],
            }
            crew: ShipCrewShape = {
                'current': ship['crew']['current'],
                'required': ship['crew']['required'],
                'capacity': ship['crew']['capacity'],
                'rotation': ship['crew']['rotation'],
                'morale': ship['crew']['morale'],
                'wages': ship['crew']['wages']
            }
            frame: ShipFrameShape = {
                'symbol': ship['frame']['symbol'],
                'name': ship['frame']['name'],
                'condition': ship['frame']['condition'],
                'integrity': ship['frame']['integrity'],
                'description': ship['frame']['description'],
                'module_slots': ship['frame']['moduleSlots'],
                'mounting_points': ship['frame']['mountingPoints'],
                'fuel_capacity': ship['frame']['fuelCapacity'],
                'requirements': ship['frame']['requirements'],
                'quality': ship['frame']['quality']
            }
            reactor: ShipReactorShape = {
                'symbol': ship['reactor']['symbol'],
                'name': ship['reactor']['name'],
                'condition': ship['reactor']['condition'],
                'integrity': ship['reactor']['integrity'],
                'description': ship['reactor']['description'],
                'power_output': ship['reactor']['powerOutput'],
                'requirements': ship['reactor']['requirements'],
                'quality': ship['reactor']['quality']
            }
            engine: ShipEngineShape = {
                'symbol': ship['engine']['symbol'],
                'name': ship['engine']['name'],
                'condition': ship['engine']['condition'],
                'integrity': ship['engine']['integrity'],
                'description': ship['engine']['description'],
                'speed': ship['engine']['speed'],
                'requirements': ship['engine']['requirements'],
                'quality': ship['engine']['quality']
            }
            modules: list[ShipModulesShape] = []
            if 'modules' in ship and ship['modules'] is not None:
                x = ship['modules']
                for module in x:
                    moduleRequirements: ShipRequirementsShape = {
                        'power': int(module['requirements']['power']),
                        'crew': int(module['requirements']['crew']),
                        'slots': int(module['requirements']['slots'])
                    }
                    modules.append(ShipModulesShape(
                        symbol=module['symbol'],
                        name=module['name'],
                        description=module['description'],
                        capacity=module['capacity'] if 'capacity' in module else 0,
                        range=module['range'] if 'range' in module else 0,
                        requirements=moduleRequirements
                    ))
            mounts: list[ShipMountsShape] = []
            if 'mounts' in ship and ship['mounts'] is not None:
                x = ship['mounts']
                for mount in x:
                    mountsRequirements: ShipRequirementsShape = {
                        'power': int(mount['requirements']['power']),
                        'crew': int(mount['requirements']['crew']),
                        'slots': int(mount['requirements']['slots']) if 'slots' in mount['requirements'] else 0
                    }
                    mountDeposits: list[ShipMountDeposits] = []
                    if 'deposits' in mount and mount['deposits'] is not None:
                        for deposit in mount['deposits']:
                            mountDeposits.append(deposit)
                    mounts.append(ShipMountsShape(
                        symbol=mount['symbol'],
                        name=mount['name'],
                        description=mount['description'],
                        strength=mount['strength'] if 'strength' in mount else 0,
                        deposits=mount['deposits'] if 'deposits' in mount else [],
                        requirements=mountsRequirements
                    ))
            inventory: list[ShipCargoInventoryShape] = []
            if 'inventory' in ship and ship['inventory'] is not None:
                inv = data['inventory']
                for item in inv:
                    inventory.append(ShipCargoInventoryShape(
                        symbol=item['symbol'],
                        name=item['name'],
                        description=item['description'],
                        units=item['units']
                    ))
            cargo: ShipCargoShape = {
                'capacity': ship['cargo']['capacity'],
                'units': ship['cargo']['units'],
                'inventory': inventory
            }
            consumed: ShipFuelConsumedShape = {
                'amount': ship['fuel']['consumed']['amount'],
                'timestamp': datetime.fromisoformat(ship['fuel']['consumed']['timestamp'])
            }
            fuel: ShipFuelShape = {
                'current': ship['fuel']['current'],
                'capacity': ship['fuel']['capacity'],
                'consumed': consumed
            }
            if 'expiration'  in ship['cooldown']:
                cooldown: ShipCooldownShape = {
                    'ship_symbol': ship['cooldown']['shipSymbol'],
                    'total_seconds': ship['cooldown']['totalSeconds'],
                    'remaining_seconds': ship['cooldown']['remainingSeconds'],
                    'expiration': datetime.fromisoformat(ship['cooldown']['expiration']) if 'expiration' not in ship['cooldown'] else datetime.fromtimestamp(0)
                }
            else:
                cooldown: ShipCooldownShape = {
                    'ship_symbol': ship['cooldown']['shipSymbol'],
                    'total_seconds': ship['cooldown']['totalSeconds'],
                    'remaining_seconds': ship['cooldown']['remainingSeconds'],
                    'expiration': datetime.fromtimestamp(0)
                }
            current_ship: ShipShape = {
                'symbol': ship['symbol'],
                'registration': registration,
                'nav': nav,
                'crew': crew,
                'frame': frame,
                'reactor': reactor,
                'engine': engine,
                'modules': modules,
                'mounts': mounts,
                'cargo': cargo,
                'fuel': fuel,
                'cooldown': cooldown
            }

            ships.append(current_ship)

        return ships if ships is not None else []
    
    def my_contracts(self) -> list[Contract]:
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.MY_CONTRACTS) \
            .call()
        
        contracts = res.spacetraders['data']

        return contracts if contracts is not None else []

    @classmethod
    def register(cls, agent_data: RegisterAgentData) -> 'Agent':
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.REGISTER) \
            .data(agent_data) \
            .call()

        match res:
            case SpaceTradersAPIResponse():
                data = res.spacetraders['data'] 
            case SpaceTradersAPIError():
                raise ValueError

        agent = data['agent']
        return cls(
            data['token'], 
            { 
                'account_id': agent['accountId'],
                'symbol': agent['symbol'],
                'headquarters': agent['headquarters'],
                'credits': int(agent['credits']),
                'starting_faction': FactionSymbol[agent['startingFaction']],
                'ship_count': int(agent['shipCount']),
            } 
        )

    @staticmethod
    def get_agent(callsign: str) -> AgentShape:
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.GET_AGENT) \
            .params(list([callsign])) \
            .call()


        agent = res.spacetraders['data']
        return { 
            # TODO: fix this, it shouldn't be in the config like this
            'account_id': CONFIG.agentID, # agent['accountId'],
            'symbol': agent['symbol'],
            'headquarters': agent['headquarters'],
            'credits': agent['credits'],
            'starting_faction': FactionSymbol[agent['startingFaction']],
            'ship_count': agent['shipCount'],
        } 

    @staticmethod
    def get_agents(
        pages: int | range = -1,
        limit: int = MAX_PAGE_LIMIT
        ) -> list[AgentShape] | SpaceTradersAPIError:

        paged_req = lambda p=1: SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.GET_AGENTS) \
            .page_number(p) \
            .call()

        # Here, -1 implies all pages, think res_pages[:-1]
        if pages == -1:
            res = paged_req()

            pages_remaining: int = int(int(res.spacetraders['meta']['total']) / limit) 

            for page in range(2, pages_remaining+1):
                res = paged_req(page)

        match pages:
            case int():
                req = paged_req(pages)
            case range():
                for page in pages:
                    req = paged_req(page)

        return []

