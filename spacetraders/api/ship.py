from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto

from spacetraders.api.api import SpaceTradersAPIRequest, SpaceTradersAPIEndpoint, SpaceTradersAPIResponse, SpaceTradersAPIError

from spacetraders.api.response import ShipCooldownShape, ShipCargoShape, ShipCargoInventoryShape
from spacetraders.api.response import ShipExtractResourceShape, ShipExtractionShape, ShipExtractShape

from spacetraders.api.response import ShipShape, ShipRegistrationShape, ShipNavShape, ShipCrewShape, ShipFrameShape, ShipReactorShape, ShipEngineShape, ShipModulesShape, ShipMountsShape, ShipCargoShape, ShipFuelShape, ShipCooldownShape, ShipCargoInventoryShape, WaypointShape, WaypointChartShape
from spacetraders.api.response import WaypointType, FactionSymbol

class Ship:

    def __init__(self):
        self.registration: ShipRegistrationShape
        self.nav: ShipNavShape
        self.crew: ShipCrewShape
        self.frame: ShipFrameShape
        self.reactor: ShipReactorShape
        self.engine: ShipEngineShape
        self.modules: ShipModulesShape
        self.mounts: ShipMountsShape
        self.cargo: ShipCargoShape
        self.fuel: ShipFuelShape
        self.cooldown: ShipCooldownShape

    @staticmethod
    def scan_waypoints(shipSymbol: str) -> list[WaypointShape]:
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.MY_SHIPS_SCAN_WAYPOINTS) \
            .params(list([shipSymbol])) \
            .call()
        
        data = res.spacetraders['data']

        match res:
            case SpaceTradersAPIResponse():
                data = res.spacetraders['data']
                # if res.spacetraders['error'] is not None:
                #     print(f'{shipSymbol} had an error while scanning waypoints.')
                #     print(f'Code: {res.spacetraders['error']['code']}, Message: {res.spacetraders['error']['message']}')
                #     return []
            case SpaceTradersAPIError():
                raise ValueError
            
        waypointShapes: list[WaypointShape] = []
        for waypoint in data['waypoints']:
            chart: WaypointChartShape = {
                'waypointSymbol': waypoint['chart']['waypointSymbol'],
                'submittedBy': waypoint['chart']['submittedBy'],
                'submittedOn': datetime.fromisoformat(waypoint['chart']['submittedOn'])
            }
            orbitals: list[str] = []
            for orbital in waypoint['orbitals']:
                orbitals.append(orbital['symbol'])
            traits = []
            if 'traits' in waypoint and waypoint['traits'] is not None:
                for trait in waypoint['traits']:
                    traits.append(trait['symbol'])
            waypointShapes.append(WaypointShape(
                symbol=waypoint['symbol'],
                type=WaypointType[waypoint['type']],
                system_symbol=waypoint['systemSymbol'],
                x=int(waypoint['x']),
                y=int(waypoint['y']),
                orbitals=orbitals,
                faction=FactionSymbol[waypoint['faction']['symbol']],
                traits=traits,
                chart=chart
            ))

        return waypointShapes if waypointShapes is not None else []
    
    @staticmethod
    def get_nav_status(shipSymbol: str):
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.MY_SHIPS_NAV) \
            .params(list([shipSymbol])) \
            .call()

        data = res.spacetraders['data']

        match res:
            case SpaceTradersAPIResponse():
                data = res.spacetraders['data']
            case SpaceTradersAPIError():
                print('value')
                raise ValueError

        return data if data is not None else []
    
    @staticmethod
    def navigate(shipSymbol: str, waypointSymbol: str):
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.MY_SHIP_NAVIGATE) \
            .params(list([shipSymbol])) \
            .data({"waypointSymbol": waypointSymbol}) \
            .call()

        data = res.spacetraders['data']
        match res:
            case SpaceTradersAPIResponse():
                data = res.spacetraders['data']
            case SpaceTradersAPIError():
                raise ValueError

        return data if data is not None else []
    
    @staticmethod
    def orbit_ship(shipSymbol: str):
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.MY_SHIPS_ORBIT) \
            .params(list([shipSymbol])) \
            .call()

        data = res.spacetraders['data']
        match res:
            case SpaceTradersAPIResponse():
                data = res.spacetraders['data']
            case SpaceTradersAPIError():
                raise ValueError

        return data if data is not None else []
    
    @staticmethod
    def dock_ship(shipSymbol: str):
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.MY_SHIPS_DOCK) \
            .params(list([shipSymbol])) \
            .call()

        data = res.spacetraders['data']
        match res:
            case SpaceTradersAPIResponse():
                data = res.spacetraders['data']
            case SpaceTradersAPIError():
                raise ValueError

        return data if data is not None else []
    
    
    @staticmethod
    def deliver_contract(contract_id: str, shipSymbol: str, tradeSymbol: str, units: int):
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.DELIVER_CONTRACT) \
            .params(list([contract_id])) \
            .data({"shipSymbol": shipSymbol.upper(),
                    "tradeSymbol": tradeSymbol.upper(),
                    "units": int(units)}) \
            .call()

        data = res.spacetraders['data']
        match res:
            case SpaceTradersAPIResponse():
                data = res.spacetraders['data']
            case SpaceTradersAPIError():
                raise ValueError

        return data if data is not None else []
    
    @staticmethod
    def purchase_cargo(shipSymbol: str, cargoSymbol: str, units):
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.MY_SHIPS_PURCHASE) \
            .params(list([shipSymbol])) \
            .data({"symbol": cargoSymbol,
                   "units": units}) \
            .call()

        data = res.spacetraders['data']
        match res:
            case SpaceTradersAPIResponse():
                data = res.spacetraders['data']
            case SpaceTradersAPIError():
                raise ValueError

        return data if data is not None else []
    
    @staticmethod
    def sell_cargo(shipSymbol: str, cargoSymbol: str, units):
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.MY_SHIPS_SELL) \
            .params(list([shipSymbol])) \
            .data({"symbol": cargoSymbol,
                   "units": units }) \
            .call()

        data = res.spacetraders['data']
        match res:
            case SpaceTradersAPIResponse():
                data = res.spacetraders['data']
            case SpaceTradersAPIError():
                raise ValueError

        return data if data is not None else []
    
    @staticmethod
    def jettison_cargo(shipSymbol: str, cargoSymbol: str, units: int) -> ShipCargoShape:
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.MY_SHIPS_JETTISON) \
            .params(list([shipSymbol])) \
            .data({"symbol": cargoSymbol,
                   "units": units}) \
            .call()

        data = res.spacetraders['data']
        match res:
            case SpaceTradersAPIResponse():
                data = res.spacetraders['data']
            case SpaceTradersAPIError():
                raise ValueError
        # Returns ShipCargoShape

        inventory: list[ShipCargoInventoryShape] = []
        if 'inventory' in data and data['inventory'] is not None:
            inv = data['inventory']
            for item in inv:
                inventory.append(ShipCargoInventoryShape(
                    symbol=item['symbol'],
                    name=item['name'],
                    description=item['description'],
                    units=item['units']
                ))

        shape: ShipCargoShape = {
            'capacity': data['capacity'],
            'units': data['units'],
            'inventory': inventory
        }
        return shape

    @staticmethod
    def extract(shipSymbol: str) -> ShipExtractShape:
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.MY_SHIPS_EXTRACT) \
            .params(list([shipSymbol])) \
            .call()

        # status 409 if ship is in cooldown, 201 if worked
        data = res.spacetraders['data']
        match res:
            case SpaceTradersAPIResponse():
                data = res.spacetraders['data']
                # if res.spacetraders['error'] is not None:
                #     print(res.spacetraders['error'])
                #     print(f'{shipSymbol} had an error while extracting.')
                #     # print(f'Code: {res.spacetraders["error"]["code"]}, Message: {res.spacetraders["error"]["message"]}')
            case SpaceTradersAPIError():
                raise ValueError
        if data is None:
            print(f'{shipSymbol} had an error while extracting.')
            error = res.spacetraders['error']
            print(f'Code: {error["code"]}, Message: {error["message"]}')
            raise ValueError(f'Extraction failed for {shipSymbol} with error code {error["code"]} and message: {error["message"]}')
        
        resource: ShipExtractResourceShape = {
            'symbol': data['extraction']['yield']['symbol'],
            'units': data['extraction']['yield']['units']
        }
        extraction: ShipExtractionShape = {
            'symbol': data['extraction']['shipSymbol'],
            'yield': resource
        }
        cooldown: ShipCooldownShape = {
            'ship_symbol': data['cooldown']['shipSymbol'],
            'total_seconds': data['cooldown']['totalSeconds'],
            'remaining_seconds': data['cooldown']['remainingSeconds'],
            'expiration': datetime.fromisoformat(data['cooldown']['expiration']) if data['cooldown']['expiration'] is not None else None
        }
        inventory: list[ShipCargoInventoryShape] = []
        if 'inventory' in data and data['inventory'] is not None:
            inv = data['inventory']
            for item in inv:
                inventory.append(ShipCargoInventoryShape(
                    symbol=item['symbol'],
                    name=item['name'],
                    description=item['description'],
                    units=item['units']
                ))
        cargo: ShipCargoShape = {
            'capacity': data['capacity'],
            'units': data['units'],
            'inventory': inventory
        }
        shape: ShipExtractShape = {
            'extraction': extraction,
            'cooldown': cooldown,
            'cargo': cargo

        }
        return shape

    @staticmethod
    def get_cooldown(shipSymbol: str) -> ShipCooldownShape:
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.MY_SHIPS_COOLDOWN) \
            .params(list([shipSymbol])) \
            .call()

        # status 200 if successfully fetched cooldowns, 204 if no cooldown
        # its going to return no content body if no cooldown
        match res:
            case SpaceTradersAPIResponse():
                data = res.spacetraders['data']
            case SpaceTradersAPIError():
                raise ValueError
            
        shape: ShipCooldownShape = {
            'ship_symbol': data['shipSymbol'],
            'total_seconds': data['totalSeconds'],
            'remaining_seconds': data['remainingSeconds'],
            'expiration': datetime.fromisoformat(data['expiration']) if data['expiration'] is not None else None
        }

        return shape if shape is not None else ShipCooldownShape(
            ship_symbol=shipSymbol,
            total_seconds=0,
            remaining_seconds=0,
            expiration=None
        )
    
    @staticmethod
    def get_cargo(shipSymbol: str) -> ShipCargoShape:
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.MY_SHIPS_CARGO) \
            .params(list([shipSymbol])) \
            .call()

        data = res.spacetraders['data']
        match res:
            case SpaceTradersAPIResponse():
                data = res.spacetraders['data']
            case SpaceTradersAPIError():
                raise ValueError
        
        inventory: list[ShipCargoInventoryShape] = []
        if 'inventory' in data and data['inventory'] is not None:
            inv = data['inventory']
            for item in inv:
                inventory.append(ShipCargoInventoryShape(
                    symbol=item['symbol'],
                    name=item['name'],
                    description=item['description'],
                    units=item['units']
                ))

        shape: ShipCargoShape = {
            'capacity': data['capacity'],
            'units': data['units'],
            'inventory': inventory
        }
        return shape if shape is not None else ShipCargoShape(
            capacity=0,
            units=0,
            inventory={}
        )
    

