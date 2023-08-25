from src.classes import *
from src.utils import *
from src.constants import NUTS3_REGION_INFO


def get_region_info(
        regions_electricity_demand: RegionsElectricityDemand
) -> RegionsElectricityDemand:

    csv_reader = CsvReader(RegionInfoReader())
    combined_region_infos = csv_reader.read(NUTS3_REGION_INFO)
    print(combined_region_infos)
    return regions_electricity_demand


def calculate_regions_electricity_demand(
        regions_electricity_demand: RegionsElectricityDemand
) -> RegionsElectricityDemand:
    get_region_info(regions_electricity_demand=regions_electricity_demand)

    return regions_electricity_demand


def main():
    regions_electricity_demand = RegionsElectricityDemand()

    calculate_regions_electricity_demand(
        regions_electricity_demand=regions_electricity_demand)

    print("Finished execution")


if __name__ == "__main__":
    main()
