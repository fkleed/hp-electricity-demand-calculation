from dataclasses import dataclass, field


@dataclass
class RegionInfo:
    nuts1_code: str
    nuts1_name: str
    nuts2_code: str
    nuts2_name: str
    nuts3_code: str
    nuts3_name: str
    nuts3_type: str


@dataclass
class BuildingInfo:
    building_type_size: str
    year_of_construction: str
    building_count: int
    hp_potential_total: float
    hp_potential_air: float
    hp_potential_probe: float
    hp_potential_collector: float
    hp_amount_air: float
    hp_amount_probe: float
    hp_amount_collector: float


@dataclass
class HourlyElectricityDemand:
    time: str
    temperature_kelvin: float
    temperature_soil_collector: float
    temperature_soil_probe: float
    hourly_electricity_demand: float


@dataclass
class Region:
    region_info: RegionInfo
    building_structure: list[BuildingInfo] = field(default_factory=list)
    electricity_demand: list[HourlyElectricityDemand] = field(
        default_factory=list)


@dataclass
class RegionsElectricityDemand:
    regions: list[Region] = field(default_factory=list)
