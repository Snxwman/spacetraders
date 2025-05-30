from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto

from spacetraders.api.faction import Faction
from spacetraders.api.api import SpaceTradersAPIRequest, SpaceTradersAPIEndpoint, SpaceTradersAPIResponse, SpaceTradersAPIError

from spacetraders.api.response import ShipCooldownShape


class Ship:

    def __init__(self):
        self.registration: ShipRegistration
        # self.nav
        self.crew: ShipCrew
        self.frame: ShipFrame
        self.reactor: ShipReactor
        self.engine: ShipEngine
        self.modules: ShipModule
        self.mounts: ShipMounts
        self.cargo: ShipCargo
        self.fuel: ShipFuel
        self.cooldown: ShipCooldown

    @staticmethod
    def scan_waypoints(shipSymbol: str) -> list[str]:
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.MY_SHIPS_SCAN_WAYPOINTS) \
            .params(list([shipSymbol])) \
            .call()
        
        data = res.spacetraders['data']

        match res:
            case SpaceTradersAPIResponse():
                data = res.spacetraders['data']
                if res.spacetraders['error'] is not None:
                    print(f'{shipSymbol} had an error while scanning waypoints.')
                    print(f'Code: {res.spacetraders['error']['code']}, Message: {res.spacetraders['error']['message']}')
                    return []
            case SpaceTradersAPIError():
                raise ValueError
        return data if data is not None else []
    
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
    def extract(shipSymbol: str):
        res = SpaceTradersAPIRequest() \
            .endpoint(SpaceTradersAPIEndpoint.MY_SHIPS_EXTRACT) \
            .params(list([shipSymbol])) \
            .call()

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

        return data if data is not None else []

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
    def get_cargo(shipSymbol: str):
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

        return data if data is not None else []
    

