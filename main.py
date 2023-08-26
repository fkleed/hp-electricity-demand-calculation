from src.classes import *
from src.utils import *
from src.constants import REGION_INFO_PATH, BUILDING_STRUCTURE_PATH, ElectricityDemandPath


def get_region_info(
        regions_electricity_demand: RegionsElectricityDemand
) -> RegionsElectricityDemand:
    csv_reader = CsvReader(RegionInfoReader())
    combined_region_infos = csv_reader.read(REGION_INFO_PATH)

    for region_info in combined_region_infos:
        regions_electricity_demand.regions[region_info.nuts3_code] = Region(
            region_info=region_info)

    return regions_electricity_demand


def get_building_structure(
        regions_electricity_demand: RegionsElectricityDemand
) -> RegionsElectricityDemand:
    csv_reader = CsvReader(BuildingStructureReader())
    combined_building_structure = csv_reader.read(BUILDING_STRUCTURE_PATH)

    for region in regions_electricity_demand.regions:
        regions_electricity_demand.regions[region].building_structure = combined_building_structure[region]

    return regions_electricity_demand


def get_hourly_electricity_demand(
        regions_electricity_demand: RegionsElectricityDemand,
        electricity_demand_path: ElectricityDemandPath
) -> RegionsElectricityDemand:
    csv_reader = CsvReader(ElectricityDemandReader())
    electricity_demand = csv_reader.read(electricity_demand_path.value)

    return regions_electricity_demand


def calculate_regions_electricity_demand(
        regions_electricity_demand: RegionsElectricityDemand,
        electricity_demand_path: ElectricityDemandPath
) -> RegionsElectricityDemand:
    get_region_info(regions_electricity_demand=regions_electricity_demand)
    get_building_structure(
        regions_electricity_demand=regions_electricity_demand)
    get_hourly_electricity_demand(
        regions_electricity_demand=regions_electricity_demand, electricity_demand_path=electricity_demand_path)

    return regions_electricity_demand


def main():
    regions_electricity_demand = RegionsElectricityDemand()

    calculate_regions_electricity_demand(
        regions_electricity_demand=regions_electricity_demand,
        electricity_demand_path=ElectricityDemandPath.REFERENCE_YEAR
    )

    print(len(regions_electricity_demand.regions))


if __name__ == "__main__":
    main()
