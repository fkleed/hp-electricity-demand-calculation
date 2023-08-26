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
    soil_temperature_kelvin_collector: float
    soil_temperature_kelvin_probe: float
    hourly_electricity_demand: float


@dataclass
class Region:
    region_info: RegionInfo
    building_structure: dict[str, BuildingInfo] = field(default_factory=dict)
    electricity_demand: dict[str, HourlyElectricityDemand] = field(
        default_factory=dict)


@dataclass
class RegionsElectricityDemand:
    regions: dict[str, Region] = field(default_factory=dict)



@dataclass
class ElectricityDemand:
    time: str
    temperature_kelvin: float
    soil_temperature_kelvin_collector: float
    soil_temperature_kelvin_probe: float
    one_and_two_family_houses_beginn_1918_ashp: float
    one_and_two_family_houses_1919_1948_ashp: float
    one_and_two_family_houses_1949_1978_ashp: float
    one_and_two_family_houses_1979_1986_ashp: float
    one_and_two_family_houses_1987_1990_ashp: float
    one_and_two_family_houses_1991_1995_ashp: float
    one_and_two_family_houses_1996_2000_ashp: float
    one_and_two_family_houses_2001_2011_ashp: float
    one_and_two_family_houses_2012_2022_ashp: float
    one_and_two_family_houses_2023_2030_ashp: float
    row_and_semi_detached_houses_beginn_1918_ashp: float
    row_and_semi_detached_houses_1919_1948_ashp: float
    row_and_semi_detached_houses_1949_1978_ashp: float
    row_and_semi_detached_houses_1979_1986_ashp: float
    row_and_semi_detached_houses_1987_1990_ashp: float
    row_and_semi_detached_houses_1991_1995_ashp: float
    row_and_semi_detached_houses_1996_2000_ashp: float
    row_and_semi_detached_houses_2001_2011_ashp: float
    row_and_semi_detached_houses_2012_2022_ashp: float
    row_and_semi_detached_houses_2023_2030_ashp: float
    apartment_buildings_3_6_beginn_1918_ashp: float
    apartment_buildings_3_6_1919_1948_ashp: float
    apartment_buildings_3_6_1949_1978_ashp: float
    apartment_buildings_3_6_1979_1986_ashp: float
    apartment_buildings_3_6_1987_1990_ashp: float
    apartment_buildings_3_6_1991_1995_ashp: float
    apartment_buildings_3_6_1996_2000_ashp: float
    apartment_buildings_3_6_2001_2011_ashp: float
    apartment_buildings_3_6_2012_2022_ashp: float
    apartment_buildings_3_6_2023_2030_ashp: float
    apartment_buildings_7_more_beginn_1918_ashp: float
    apartment_buildings_7_more_1919_1948_ashp: float
    apartment_buildings_7_more_1949_1978_ashp: float
    apartment_buildings_7_more_1979_1986_ashp: float
    apartment_buildings_7_more_1987_1990_ashp: float
    apartment_buildings_7_more_1991_1995_ashp: float
    apartment_buildings_7_more_1996_2000_ashp: float
    apartment_buildings_7_more_2001_2011_ashp: float
    apartment_buildings_7_more_2012_2022_ashp: float
    apartment_buildings_7_more_2023_2030_ashp: float
    one_and_two_family_houses_beginn_1918_gshp_collector: float
    one_and_two_family_houses_1919_1948_gshp_collector: float
    one_and_two_family_houses_1949_1978_gshp_collector: float
    one_and_two_family_houses_1979_1986_gshp_collector: float
    one_and_two_family_houses_1987_1990_gshp_collector: float
    one_and_two_family_houses_1991_1995_gshp_collector: float
    one_and_two_family_houses_1996_2000_gshp_collector: float
    one_and_two_family_houses_2001_2011_gshp_collector: float
    one_and_two_family_houses_2012_2022_gshp_collector: float
    one_and_two_family_houses_2023_2030_gshp_collector: float
    row_and_semi_detached_houses_beginn_1918_gshp_collector: float
    row_and_semi_detached_houses_1919_1948_gshp_collector: float
    row_and_semi_detached_houses_1949_1978_gshp_collector: float
    row_and_semi_detached_houses_1979_1986_gshp_collector: float
    row_and_semi_detached_houses_1987_1990_gshp_collector: float
    row_and_semi_detached_houses_1991_1995_gshp_collector: float
    row_and_semi_detached_houses_1996_2000_gshp_collector: float
    row_and_semi_detached_houses_2001_2011_gshp_collector: float
    row_and_semi_detached_houses_2012_2022_gshp_collector: float
    row_and_semi_detached_houses_2023_2030_gshp_collector: float
    apartment_buildings_3_6_beginn_1918_gshp_collector: float
    apartment_buildings_3_6_1919_1948_gshp_collector: float
    apartment_buildings_3_6_1949_1978_gshp_collector: float
    apartment_buildings_3_6_1979_1986_gshp_collector: float
    apartment_buildings_3_6_1987_1990_gshp_collector: float
    apartment_buildings_3_6_1991_1995_gshp_collector: float
    apartment_buildings_3_6_1996_2000_gshp_collector: float
    apartment_buildings_3_6_2001_2011_gshp_collector: float
    apartment_buildings_3_6_2012_2022_gshp_collector: float
    apartment_buildings_3_6_2023_2030_gshp_collector: float
    apartment_buildings_7_more_beginn_1918_gshp_collector: float
    apartment_buildings_7_more_1919_1948_gshp_collector: float
    apartment_buildings_7_more_1949_1978_gshp_collector: float
    apartment_buildings_7_more_1979_1986_gshp_collector: float
    apartment_buildings_7_more_1987_1990_gshp_collector: float
    apartment_buildings_7_more_1991_1995_gshp_collector: float
    apartment_buildings_7_more_1996_2000_gshp_collector: float
    apartment_buildings_7_more_2001_2011_gshp_collector: float
    apartment_buildings_7_more_2012_2022_gshp_collector: float
    apartment_buildings_7_more_2023_2030_gshp_collector: float
    one_and_two_family_houses_beginn_1918_gshp_probe: float
    one_and_two_family_houses_1919_1948_gshp_probe: float
    one_and_two_family_houses_1949_1978_gshp_probe: float
    one_and_two_family_houses_1979_1986_gshp_probe: float
    one_and_two_family_houses_1987_1990_gshp_probe: float
    one_and_two_family_houses_1991_1995_gshp_probe: float
    one_and_two_family_houses_1996_2000_gshp_probe: float
    one_and_two_family_houses_2001_2011_gshp_probe: float
    one_and_two_family_houses_2012_2022_gshp_probe: float
    one_and_two_family_houses_2023_2030_gshp_probe: float
    row_and_semi_detached_houses_beginn_1918_gshp_probe: float
    row_and_semi_detached_houses_1919_1948_gshp_probe: float
    row_and_semi_detached_houses_1949_1978_gshp_probe: float
    row_and_semi_detached_houses_1979_1986_gshp_probe: float
    row_and_semi_detached_houses_1987_1990_gshp_probe: float
    row_and_semi_detached_houses_1991_1995_gshp_probe: float
    row_and_semi_detached_houses_1996_2000_gshp_probe: float
    row_and_semi_detached_houses_2001_2011_gshp_probe: float
    row_and_semi_detached_houses_2012_2022_gshp_probe: float
    row_and_semi_detached_houses_2023_2030_gshp_probe: float
    apartment_buildings_3_6_beginn_1918_gshp_probe: float
    apartment_buildings_3_6_1919_1948_gshp_probe: float
    apartment_buildings_3_6_1949_1978_gshp_probe: float
    apartment_buildings_3_6_1979_1986_gshp_probe: float
    apartment_buildings_3_6_1987_1990_gshp_probe: float
    apartment_buildings_3_6_1991_1995_gshp_probe: float
    apartment_buildings_3_6_1996_2000_gshp_probe: float
    apartment_buildings_3_6_2001_2011_gshp_probe: float
    apartment_buildings_3_6_2012_2022_gshp_probe: float
    apartment_buildings_3_6_2023_2030_gshp_probe: float
    apartment_buildings_7_more_beginn_1918_gshp_probe: float
    apartment_buildings_7_more_1919_1948_gshp_probe: float
    apartment_buildings_7_more_1949_1978_gshp_probe: float
    apartment_buildings_7_more_1979_1986_gshp_probe: float
    apartment_buildings_7_more_1987_1990_gshp_probe: float
    apartment_buildings_7_more_1991_1995_gshp_probe: float
    apartment_buildings_7_more_1996_2000_gshp_probe: float
    apartment_buildings_7_more_2001_2011_gshp_probe: float
    apartment_buildings_7_more_2012_2022_gshp_probe: float
    apartment_buildings_7_more_2023_2030_gshp_probe: float