from src.classes import *
from src.utils import *
from src.constants import REGION_INFO_PATH, BUILDING_INFO_PATH


def get_region_info(
        regions_electricity_demand: RegionsElectricityDemand
) -> RegionsElectricityDemand:
    csv_reader = CsvReader(RegionInfoReader())
    combined_region_infos = csv_reader.read(REGION_INFO_PATH)

    for region_info in combined_region_infos:
        regions_electricity_demand.regions.append(
            Region(
                region_info
            )
        )

    return regions_electricity_demand


def get_building_info(
        regions_electricity_demand: RegionsElectricityDemand
) -> RegionsElectricityDemand:
    csv_reader = CsvReader(BuildingInfoReader())
    combined_building_info = csv_reader.read(BUILDING_INFO_PATH)

    for region in regions_electricity_demand.regions:
        region.building_structure = combined_building_info[region.region_info.nuts3_code]

    return regions_electricity_demand


def calculate_regions_electricity_demand(
        regions_electricity_demand: RegionsElectricityDemand
) -> RegionsElectricityDemand:
    get_region_info(regions_electricity_demand=regions_electricity_demand)
    get_building_info(regions_electricity_demand=regions_electricity_demand)

    return regions_electricity_demand


def main():
    regions_electricity_demand = RegionsElectricityDemand()

    calculate_regions_electricity_demand(
        regions_electricity_demand=regions_electricity_demand)

    print(len(regions_electricity_demand.regions))


if __name__ == "__main__":
    main()
