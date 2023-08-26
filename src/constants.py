from enum import Enum

REGION_INFO_PATH = "./data/regioninfo/nuts3regioninfo.csv"
BUILDING_STRUCTURE_PATH = "./data/hpdistribution/building_stock_2030_with_hp_distribution.csv"


class ElectricityDemandPath(Enum):
    REFERENCE_YEAR = "./data/electricitydemand/loadprofile_reference.csv"
    COLD_YEAR = "./data/electricitydemand/loadprofile_cold.csv"
    HOT_YEAR = "./data/electricitydemand/loadprofile_hot.csv"
    REFERENCE_YEAR_SPACE_HEAT_ONLY = "./data/electricitydemand/loadprofile_space_heat_only_reference.csv"
    COLD_YEAR_SPACE_HEAT_ONLY = "./data/electricitydemand/loadprofile_space_heat_only_cold.csv"
    HOT_YEAR_SPACE_HEAT_ONLY = "./data/electricitydemand/loadprofile_space_heat_only_hot.csv"
