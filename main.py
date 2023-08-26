from src.classes import RegionsElectricityDemand
from src.calculations import calculate_regions_electricity_demand
from src.constants import ElectricityDemandPath



def main():
    regions_electricity_demand = RegionsElectricityDemand()

    calculate_regions_electricity_demand(
        regions_electricity_demand=regions_electricity_demand,
        electricity_demand_path=ElectricityDemandPath.REFERENCE_YEAR
    )

    print(len(regions_electricity_demand.regions))


if __name__ == "__main__":
    main()
