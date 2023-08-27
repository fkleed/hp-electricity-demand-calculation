from src.classes import RegionsElectricityDemand
from src.calculations import calculate_regions_electricity_demand
from src.constants import ElectricityDemandPath, RegionsElectricityDemandOutputPath
from src.utils import CsvWriter, RegionsElectricityDemandWriter


def write_electricity_demand_to_csv(regions_electricity_demand: RegionsElectricityDemand, regions_electricity_demand_output_path: RegionsElectricityDemandOutputPath):
    writer = CsvWriter(RegionsElectricityDemandWriter())
    writer.write(regions_electricity_demand,
                 regions_electricity_demand_output_path.value)


def main():
    regions_electricity_demand = RegionsElectricityDemand()

    calculate_regions_electricity_demand(
        regions_electricity_demand=regions_electricity_demand,
        electricity_demand_path=ElectricityDemandPath.REFERENCE_YEAR
    )

    write_electricity_demand_to_csv(
        regions_electricity_demand=regions_electricity_demand,
        regions_electricity_demand_output_path=RegionsElectricityDemandOutputPath.REFERENCE_YEAR
    )


if __name__ == "__main__":
    main()
