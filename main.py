from src.classes import RegionsElectricityDemand
from src.calculations import calculate_regions_electricity_demand
from src.constants import ElectricityDemandPath, RegionsElectricityDemandOutputPath
from src.utils import DataSerializer, JsonSerializer


def write_electricity_demand_to_json(regions_electricity_demand: RegionsElectricityDemand, regions_electricity_demand_output_path: RegionsElectricityDemandOutputPath):
    serializer = DataSerializer(JsonSerializer())
    serialized_data = serializer.serialize(regions_electricity_demand)

    with open(regions_electricity_demand_output_path.value, "w") as output_file:
        output_file.write(serialized_data)


def main():
    regions_electricity_demand = RegionsElectricityDemand()

    calculate_regions_electricity_demand(
        regions_electricity_demand=regions_electricity_demand,
        electricity_demand_path=ElectricityDemandPath.REFERENCE_YEAR
    )

    write_electricity_demand_to_json(
        regions_electricity_demand=regions_electricity_demand,
        regions_electricity_demand_output_path=RegionsElectricityDemandOutputPath.REFERENCE_YEAR
    )


if __name__ == "__main__":
    main()
