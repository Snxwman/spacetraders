from __future__ import annotations

from enum import Enum


class ShipComponent(Enum):
    """

    FRAME
    REACTOR
    ENGINE
    """

    FRAME = 'FRAME'
    REACTOR = 'REACTOR'
    ENGINE = 'ENGINE'


class ShipConditionEvent(Enum):
    """

    ATMOSPHERIC_ENTRY_HEAT
    BEARING_LUBRICATION_FADE
    COOLANT_LEAK
    COOLANT_SYSTEM_AGEING
    CORROSIVE_MINERAL_CONTAMINATION
    DUST_MICROABRASIONS
    ELECTROMAGNETIC_FIELD_INTERFERENCE
    ELECTROMAGNETIC_SURGE_EFFECTS
    ENERGY_SPIKE_FROM_MINERAL
    EXHAUST_PORT_CLOGGING
    FUEL_EFFICIENCY_DEGRADATION
    HULL_MICROMETEORITE_DAMAGE
    HULL_MICROMETEORITE_STRIKES
    IMPACT_WITH_EXTRACTED_DEBRIS
    MAGNETIC_FIELD_DISRUPTION
    POWER_DISTRIBUTION_FLUCTUATION
    PRESSURE_DIFFERENTIAL_STRESS
    REACTOR_OVERLOAD
    SENSOR_CALIBRATION_DRIFT
    SOLAR_FLARE_INTERFERENCE
    SPACE_DEBRIS_COLLISION
    STRUCTURAL_STRESS_FRACTURES
    THERMAL_EXPANSION_MISMATCH
    THERMAL_STRESS
    THRUSTER_NOZZLE_WEAR
    VIBRATION_DAMAGE_FROM_DRILLING
    VIBRATION_OVERLOAD
    """

    ATMOSPHERIC_ENTRY_HEAT = 'ATMOSPHERIC_ENTRY_HEAT'
    BEARING_LUBRICATION_FADE = 'BEARING_LUBRICATION_FADE'
    COOLANT_LEAK = 'COOLANT_LEAK'
    COOLANT_SYSTEM_AGEING = 'COOLANT_SYSTEM_AGEING'
    CORROSIVE_MINERAL_CONTAMINATION = 'CORROSIVE_MINERAL_CONTAMINATION'
    DUST_MICROABRASIONS = 'DUST_MICROABRASIONS'
    ELECTROMAGNETIC_FIELD_INTERFERENCE = 'ELECTROMAGNETIC_FIELD_INTERFERENCE'
    ELECTROMAGNETIC_SURGE_EFFECTS = 'ELECTROMAGNETIC_SURGE_EFFECTS'
    ENERGY_SPIKE_FROM_MINERAL = 'ENERGY_SPIKE_FROM_MINERAL'
    EXHAUST_PORT_CLOGGING = 'EXHAUST_PORT_CLOGGING'
    FUEL_EFFICIENCY_DEGRADATION = 'FUEL_EFFICIENCY_DEGRADATION'
    HULL_MICROMETEORITE_DAMAGE = 'HULL_MICROMETEORITE_DAMAGE'
    HULL_MICROMETEORITE_STRIKES = 'HULL_MICROMETEORITE_STRIKES'
    IMPACT_WITH_EXTRACTED_DEBRIS = 'IMPACT_WITH_EXTRACTED_DEBRIS'
    MAGNETIC_FIELD_DISRUPTION = 'MAGNETIC_FIELD_DISRUPTION'
    POWER_DISTRIBUTION_FLUCTUATION = 'POWER_DISTRIBUTION_FLUCTUATION'
    PRESSURE_DIFFERENTIAL_STRESS = 'PRESSURE_DIFFERENTIAL_STRESS'
    REACTOR_OVERLOAD = 'REACTOR_OVERLOAD'
    SENSOR_CALIBRATION_DRIFT = 'SENSOR_CALIBRATION_DRIFT'
    SOLAR_FLARE_INTERFERENCE = 'SOLAR_FLARE_INTERFERENCE'
    SPACE_DEBRIS_COLLISION = 'SPACE_DEBRIS_COLLISION'
    STRUCTURAL_STRESS_FRACTURES = 'STRUCTURAL_STRESS_FRACTURES'
    THERMAL_EXPANSION_MISMATCH = 'THERMAL_EXPANSION_MISMATCH'
    THERMAL_STRESS = 'THERMAL_STRESS'
    THRUSTER_NOZZLE_WEAR = 'THRUSTER_NOZZLE_WEAR'
    VIBRATION_DAMAGE_FROM_DRILLING = 'VIBRATION_DAMAGE_FROM_DRILLING'
    VIBRATION_OVERLOAD = 'VIBRATION_OVERLOAD'


class ShipCrewRotationShape(Enum):
    """

    STRICT
    RELAXED
    """

    STRICT = 'STRICT'
    RELAXED = 'RELAXED'


class ShipEngines(Enum):
    """

    ENGINE_HYPER_DRIVE_I
    ENGINE_IMPULSE_DRIVE_I
    ENGINE_ION_DRIVE_I
    ENGINE_ION_DRIVE_II
    """

    ENGINE_HYPER_DRIVE_I = 'ENGINE_HYPER_DRIVE_I'
    ENGINE_IMPULSE_DRIVE_I = 'ENGINE_IMPULSE_DRIVE_I'
    ENGINE_ION_DRIVE_I = 'ENGINE_ION_DRIVE_I'
    ENGINE_ION_DRIVE_II = 'ENGINE_ION_DRIVE_II'


class ShipFrames(Enum):
    """

    FRAME_BULK_FREIGHTER
    FRAME_CARRIER
    FRAME_CRUISER
    FRAME_DESTROYER
    FRAME_DRONE
    FRAME_EXPLORER
    FRAME_FIGHTER
    FRAME_FRIGATE
    FRAME_HEAVY_FREIGHTER
    FRAME_INTERCEPTOR
    FRAME_LIGHT_FREIGHTER
    FRAME_MINER
    FRAME_PROBE
    FRAME_RACER
    FRAME_SHUTTLE
    FRAME_TRANSPORT
    """

    FRAME_BULK_FREIGHTER = 'FRAME_BULK_FREIGHTER'
    FRAME_CARRIER = 'FRAME_CARRIER'
    FRAME_CRUISER = 'FRAME_CRUISER'
    FRAME_DESTROYER = 'FRAME_DESTROYER'
    FRAME_DRONE = 'FRAME_DRONE'
    FRAME_EXPLORER = 'FRAME_EXPLORER'
    FRAME_FIGHTER = 'FRAME_FIGHTER'
    FRAME_FRIGATE = 'FRAME_FRIGATE'
    FRAME_HEAVY_FREIGHTER = 'FRAME_HEAVY_FREIGHTER'
    FRAME_INTERCEPTOR = 'FRAME_INTERCEPTOR'
    FRAME_LIGHT_FREIGHTER = 'FRAME_LIGHT_FREIGHTER'
    FRAME_MINER = 'FRAME_MINER'
    FRAME_PROBE = 'FRAME_PROBE'
    FRAME_RACER = 'FRAME_RACER'
    FRAME_SHUTTLE = 'FRAME_SHUTTLE'
    FRAME_TRANSPORT = 'FRAME_TRANSPORT'


class ShipModules(Enum):
    """

    MODULE_CARGO_HOLD_I
    MODULE_CARGO_HOLD_II
    MODULE_CARGO_HOLD_III
    MODULE_CREW_QUARTERS_I
    MODULE_ENVOY_QUARTERS_I
    MODULE_FUEL_REFINERY_I
    MODULE_GAS_PROCESSOR_I
    MODULE_JUMP_DRIVE_I
    MODULE_JUMP_DRIVE_II
    MODULE_JUMP_DRIVE_III
    MODULE_MICRO_REFINERY_I
    MODULE_MINERAL_PROCESSOR_I
    MODULE_ORE_REFINERY_I
    MODULE_PASSENGER_CABIN_I
    MODULE_SCIENCE_LAB_I
    MODULE_SHIELD_GENERATOR_I
    MODULE_SHIELD_GENERATOR_II
    MODULE_WARP_DRIVE_I
    MODULE_WARP_DRIVE_II
    MODULE_WARP_DRIVE_III
    """

    MODULE_CARGO_HOLD_I = 'MODULE_CARGO_HOLD_I'
    MODULE_CARGO_HOLD_II = 'MODULE_CARGO_HOLD_II'
    MODULE_CARGO_HOLD_III = 'MODULE_CARGO_HOLD_III'
    MODULE_CREW_QUARTERS_I = 'MODULE_CREW_QUARTERS_I'
    MODULE_ENVOY_QUARTERS_I = 'MODULE_ENVOY_QUARTERS_I'
    MODULE_FUEL_REFINERY_I = 'MODULE_FUEL_REFINERY_I'
    MODULE_GAS_PROCESSOR_I = 'MODULE_GAS_PROCESSOR_I'
    MODULE_JUMP_DRIVE_I = 'MODULE_JUMP_DRIVE_I'
    MODULE_JUMP_DRIVE_II = 'MODULE_JUMP_DRIVE_II'
    MODULE_JUMP_DRIVE_III = 'MODULE_JUMP_DRIVE_III'
    MODULE_MICRO_REFINERY_I = 'MODULE_MICRO_REFINERY_I'
    MODULE_MINERAL_PROCESSOR_I = 'MODULE_MINERAL_PROCESSOR_I'
    MODULE_ORE_REFINERY_I = 'MODULE_ORE_REFINERY_I'
    MODULE_PASSENGER_CABIN_I = 'MODULE_PASSENGER_CABIN_I'
    MODULE_SCIENCE_LAB_I = 'MODULE_SCIENCE_LAB_I'
    MODULE_SHIELD_GENERATOR_I = 'MODULE_SHIELD_GENERATOR_I'
    MODULE_SHIELD_GENERATOR_II = 'MODULE_SHIELD_GENERATOR_II'
    MODULE_WARP_DRIVE_I = 'MODULE_WARP_DRIVE_I'
    MODULE_WARP_DRIVE_II = 'MODULE_WARP_DRIVE_II'
    MODULE_WARP_DRIVE_III = 'MODULE_WARP_DRIVE_III'


class ShipMounts(Enum):
    """

    MOUNT_GAS_SIPHON_I
    MOUNT_GAS_SIPHON_II
    MOUNT_GAS_SIPHON_III
    MOUNT_LASER_CANNON_I
    MOUNT_MINING_LASER_I
    MOUNT_MINING_LASER_II
    MOUNT_MINING_LASER_III
    MOUNT_MISSILE_LAUNCHER_I
    MOUNT_SENSOR_ARRAY_I
    MOUNT_SENSOR_ARRAY_II
    MOUNT_SENSOR_ARRAY_III
    MOUNT_SURVEYOR_I
    MOUNT_SURVEYOR_II
    MOUNT_SURVEYOR_III
    MOUNT_TURRET_I
    """

    MOUNT_GAS_SIPHON_I = 'MOUNT_GAS_SIPHON_I'
    MOUNT_GAS_SIPHON_II = 'MOUNT_GAS_SIPHON_II'
    MOUNT_GAS_SIPHON_III = 'MOUNT_GAS_SIPHON_III'
    MOUNT_LASER_CANNON_I = 'MOUNT_LASER_CANNON_I'
    MOUNT_MINING_LASER_I = 'MOUNT_MINING_LASER_I'
    MOUNT_MINING_LASER_II = 'MOUNT_MINING_LASER_II'
    MOUNT_MINING_LASER_III = 'MOUNT_MINING_LASER_III'
    MOUNT_MISSILE_LAUNCHER_I = 'MOUNT_MISSILE_LAUNCHER_I'
    MOUNT_SENSOR_ARRAY_I = 'MOUNT_SENSOR_ARRAY_I'
    MOUNT_SENSOR_ARRAY_II = 'MOUNT_SENSOR_ARRAY_II'
    MOUNT_SENSOR_ARRAY_III = 'MOUNT_SENSOR_ARRAY_III'
    MOUNT_SURVEYOR_I = 'MOUNT_SURVEYOR_I'
    MOUNT_SURVEYOR_II = 'MOUNT_SURVEYOR_II'
    MOUNT_SURVEYOR_III = 'MOUNT_SURVEYOR_III'
    MOUNT_TURRET_I = 'MOUNT_TURRET_I'


class ShipMountDeposits(Enum):
    """

    ALUMINUM_ORE
    AMMONIA_ICE
    COPPER_ORE
    DIAMONDS
    GOLD_ORE
    ICE_WATER
    IRON_ORE
    MERITIUM_ORE
    PLATINUM_ORE
    PRECIOUS_STONES
    QUARTZ_SAND
    SILICON_CRYSTALS
    SILVER_ORE
    URANITE_ORE
    """

    ALUMINUM_ORE = 'ALUMINUM_ORE'
    AMMONIA_ICE = 'AMMONIA_ICE'
    COPPER_ORE = 'COPPER_ORE'
    DIAMONDS = 'DIAMONDS'
    GOLD_ORE = 'GOLD_ORE'
    ICE_WATER = 'ICE_WATER'
    IRON_ORE = 'IRON_ORE'
    MERITIUM_ORE = 'MERITIUM_ORE'
    PLATINUM_ORE = 'PLATINUM_ORE'
    PRECIOUS_STONES = 'PRECIOUS_STONES'
    QUARTZ_SAND = 'QUARTZ_SAND'
    SILICON_CRYSTALS = 'SILICON_CRYSTALS'
    SILVER_ORE = 'SILVER_ORE'
    URANITE_ORE = 'URANITE_ORE'


class ShipNavFlightMode(Enum):
    """

    BURN
    CRUISE
    DRIFT
    STEALTH
    """

    BURN = 'BURN'
    CRUISE = 'CRUISE'
    DRIFT = 'DRIFT'
    STEALTH = 'STEALTH'


class ShipNavStatus(Enum):
    """

    DOCKED
    IN_ORBIT
    IN_TRANSIT
    """

    DOCKED = 'DOCKED'
    IN_ORBIT = 'IN_ORBIT'
    IN_TRANSIT = 'IN_TRANSIT'


class ShipReactors(Enum):
    """

    REACTOR_ANTIMATTER_I
    REACTOR_CHEMICAL_I
    REACTOR_FISSION_I
    REACTOR_FUSION_I
    REACTOR_SOLAR_I
    """

    REACTOR_ANTIMATTER_I = 'REACTOR_ANTIMATTER_I'
    REACTOR_CHEMICAL_I = 'REACTOR_CHEMICAL_I'
    REACTOR_FISSION_I = 'REACTOR_FISSION_I'
    REACTOR_FUSION_I = 'REACTOR_FUSION_I'
    REACTOR_SOLAR_I = 'REACTOR_SOLAR_I'


class ShipRole(Enum):
    """

    CARRIER
    COMMAND
    EXCAVATOR
    EXPLORER
    FABRICATOR
    HARVESTER
    HAULER
    INTERCEPTOR
    PATROL
    REFINERY
    REPAIR
    SATELLITE
    SURVEYOR
    TRANSPORT
    """

    CARRIER = 'CARRIER'
    COMMAND = 'COMMAND'
    EXCAVATOR = 'EXCAVATOR'
    EXPLORER = 'EXPLORER'
    FABRICATOR = 'FABRICATOR'
    HARVESTER = 'HARVESTER'
    HAULER = 'HAULER'
    INTERCEPTOR = 'INTERCEPTOR'
    PATROL = 'PATROL'
    REFINERY = 'REFINERY'
    REPAIR = 'REPAIR'
    SATELLITE = 'SATELLITE'
    SURVEYOR = 'SURVEYOR'
    TRANSPORT = 'TRANSPORT'


class ShipType(Enum):
    """

    SHIP_BULK_FREIGHTER
    SHIP_COMMAND_FRIGATE
    SHIP_EXPLORER
    SHIP_HEAVY_FREIGHTER
    SHIP_INTERCEPTOR
    SHIP_LIGHT_HAULER
    SHIP_LIGHT_SHUTTLE
    SHIP_MINING_DRONE
    SHIP_ORE_HOUND
    SHIP_PROBE
    SHIP_REFINING_FREIGHTER
    SHIP_SIPHON_DRONE
    SHIP_SURVEYOR
    """

    SHIP_BULK_FREIGHTER = 'SHIP_BULK_FREIGHTER'
    SHIP_COMMAND_FRIGATE = 'SHIP_COMMAND_FRIGATE'
    SHIP_EXPLORER = 'SHIP_EXPLORER'
    SHIP_HEAVY_FREIGHTER = 'SHIP_HEAVY_FREIGHTER'
    SHIP_INTERCEPTOR = 'SHIP_INTERCEPTOR'
    SHIP_LIGHT_HAULER = 'SHIP_LIGHT_HAULER'
    SHIP_LIGHT_SHUTTLE = 'SHIP_LIGHT_SHUTTLE'
    SHIP_MINING_DRONE = 'SHIP_MINING_DRONE'
    SHIP_ORE_HOUND = 'SHIP_ORE_HOUND'
    SHIP_PROBE = 'SHIP_PROBE'
    SHIP_REFINING_FREIGHTER = 'SHIP_REFINING_FREIGHTER'
    SHIP_SIPHON_DRONE = 'SHIP_SIPHON_DRONE'
    SHIP_SURVEYOR = 'SHIP_SURVEYOR'
