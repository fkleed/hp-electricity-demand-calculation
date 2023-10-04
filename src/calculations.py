from src.classes import *
from src.utils import *
from src.constants import BUILDING_STRUCTURE_PATH, ElectricityDemandPath


def get_building_structure() -> dict[str, dict[str, BuildingInfo]]:
    csv_reader = CsvReader(BuildingStructureReader())
    return csv_reader.read(BUILDING_STRUCTURE_PATH)


def get_hourly_electricity_demand(
        regions_electricity_demand: RegionsElectricityDemand,
        electricity_demand_path: ElectricityDemandPath,
        combined_building_structure: dict[str, dict[str, BuildingInfo]]
) -> dict[str, HourlyElectricityDemand]:
    csv_reader = CsvReader(ElectricityDemandReader())
    electricity_demand_building_types = csv_reader.read(
        electricity_demand_path.value)

    regions = list(combined_building_structure.keys())

    for region in regions:
        electricity_demand: dict[str, HourlyElectricityDemand] = dict()
        building_structure = combined_building_structure[region]

        # ashp
        one_and_two_family_houses_beginn_1918_ashp_amount = building_structure[
            'One- and Two-family Houses' + ' ' + 'Before 1919'].hp_amount_air
        one_and_two_family_houses_1919_1948_ashp_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1919 - 1948'].hp_amount_air
        one_and_two_family_houses_1949_1978_ashp_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1949 - 1978'].hp_amount_air
        one_and_two_family_houses_1979_1986_ashp_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1979 - 1986'].hp_amount_air
        one_and_two_family_houses_1987_1990_ashp_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1987 - 1990'].hp_amount_air
        one_and_two_family_houses_1991_1995_ashp_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1991 - 1995'].hp_amount_air
        one_and_two_family_houses_1996_2000_ashp_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1996 - 2000'].hp_amount_air
        one_and_two_family_houses_2001_2011_ashp_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '2001 - 2011'].hp_amount_air
        one_and_two_family_houses_2012_2022_ashp_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '2012 - 2022'].hp_amount_air
        one_and_two_family_houses_2023_2030_ashp_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '2023 - 2030'].hp_amount_air
        row_houses_beginn_1918_ashp_amount = building_structure['Row Houses' +
                                                                ' ' + 'Before 1919'].hp_amount_air
        row_houses_1919_1948_ashp_amount = building_structure['Row Houses' +
                                                              ' ' + '1919 - 1948'].hp_amount_air
        row_houses_1949_1978_ashp_amount = building_structure['Row Houses' +
                                                              ' ' + '1949 - 1978'].hp_amount_air
        row_houses_1979_1986_ashp_amount = building_structure['Row Houses' +
                                                              ' ' + '1979 - 1986'].hp_amount_air
        row_houses_1987_1990_ashp_amount = building_structure['Row Houses' +
                                                              ' ' + '1987 - 1990'].hp_amount_air
        row_houses_1991_1995_ashp_amount = building_structure['Row Houses' +
                                                              ' ' + '1991 - 1995'].hp_amount_air
        row_houses_1996_2000_ashp_amount = building_structure['Row Houses' +
                                                              ' ' + '1996 - 2000'].hp_amount_air
        row_houses_2001_2011_ashp_amount = building_structure['Row Houses' +
                                                              ' ' + '2001 - 2011'].hp_amount_air
        row_houses_2012_2022_ashp_amount = building_structure['Row Houses' +
                                                              ' ' + '2012 - 2022'].hp_amount_air
        row_houses_2023_2030_ashp_amount = building_structure['Row Houses' +
                                                              ' ' + '2023 - 2030'].hp_amount_air
        semi_detached_houses_beginn_1918_ashp_amount = building_structure[
            'Semi-detached Houses' + ' ' + 'Before 1919'].hp_amount_air
        semi_detached_houses_1919_1948_ashp_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1919 - 1948'].hp_amount_air
        semi_detached_houses_1949_1978_ashp_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1949 - 1978'].hp_amount_air
        semi_detached_houses_1979_1986_ashp_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1979 - 1986'].hp_amount_air
        semi_detached_houses_1987_1990_ashp_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1987 - 1990'].hp_amount_air
        semi_detached_houses_1991_1995_ashp_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1991 - 1995'].hp_amount_air
        semi_detached_houses_1996_2000_ashp_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1996 - 2000'].hp_amount_air
        semi_detached_houses_2001_2011_ashp_amount = building_structure[
            'Semi-detached Houses' + ' ' + '2001 - 2011'].hp_amount_air
        semi_detached_houses_2012_2022_ashp_amount = building_structure[
            'Semi-detached Houses' + ' ' + '2012 - 2022'].hp_amount_air
        semi_detached_houses_2023_2030_ashp_amount = building_structure[
            'Semi-detached Houses' + ' ' + '2023 - 2030'].hp_amount_air
        apartment_buildings_3_6_beginn_1918_ashp_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + 'Before 1919'].hp_amount_air
        apartment_buildings_3_6_1919_1948_ashp_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1919 - 1948'].hp_amount_air
        apartment_buildings_3_6_1949_1978_ashp_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1949 - 1978'].hp_amount_air
        apartment_buildings_3_6_1979_1986_ashp_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1979 - 1986'].hp_amount_air
        apartment_buildings_3_6_1987_1990_ashp_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1987 - 1990'].hp_amount_air
        apartment_buildings_3_6_1991_1995_ashp_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1991 - 1995'].hp_amount_air
        apartment_buildings_3_6_1996_2000_ashp_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1996 - 2000'].hp_amount_air
        apartment_buildings_3_6_2001_2011_ashp_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '2001 - 2011'].hp_amount_air
        apartment_buildings_3_6_2012_2022_ashp_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '2012 - 2022'].hp_amount_air
        apartment_buildings_3_6_2023_2030_ashp_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '2023 - 2030'].hp_amount_air
        apartment_buildings_7_more_beginn_1918_ashp_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + 'Before 1919'].hp_amount_air
        apartment_buildings_7_more_1919_1948_ashp_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1919 - 1948'].hp_amount_air
        apartment_buildings_7_more_1949_1978_ashp_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1949 - 1978'].hp_amount_air
        apartment_buildings_7_more_1979_1986_ashp_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1979 - 1986'].hp_amount_air
        apartment_buildings_7_more_1987_1990_ashp_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1987 - 1990'].hp_amount_air
        apartment_buildings_7_more_1991_1995_ashp_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1991 - 1995'].hp_amount_air
        apartment_buildings_7_more_1996_2000_ashp_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1996 - 2000'].hp_amount_air
        apartment_buildings_7_more_2001_2011_ashp_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '2001 - 2011'].hp_amount_air
        apartment_buildings_7_more_2012_2022_ashp_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '2012 - 2022'].hp_amount_air
        apartment_buildings_7_more_2023_2030_ashp_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '2023 - 2030'].hp_amount_air

        # gshp collector
        one_and_two_family_houses_beginn_1918_gshp_collector_amount = building_structure[
            'One- and Two-family Houses' + ' ' + 'Before 1919'].hp_amount_collector
        one_and_two_family_houses_1919_1948_gshp_collector_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1919 - 1948'].hp_amount_collector
        one_and_two_family_houses_1949_1978_gshp_collector_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1949 - 1978'].hp_amount_collector
        one_and_two_family_houses_1979_1986_gshp_collector_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1979 - 1986'].hp_amount_collector
        one_and_two_family_houses_1987_1990_gshp_collector_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1987 - 1990'].hp_amount_collector
        one_and_two_family_houses_1991_1995_gshp_collector_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1991 - 1995'].hp_amount_collector
        one_and_two_family_houses_1996_2000_gshp_collector_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1996 - 2000'].hp_amount_collector
        one_and_two_family_houses_2001_2011_gshp_collector_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '2001 - 2011'].hp_amount_collector
        one_and_two_family_houses_2012_2022_gshp_collector_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '2012 - 2022'].hp_amount_collector
        one_and_two_family_houses_2023_2030_gshp_collector_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '2023 - 2030'].hp_amount_collector
        row_houses_beginn_1918_gshp_collector_amount = building_structure[
            'Row Houses' + ' ' + 'Before 1919'].hp_amount_collector
        row_houses_1919_1948_gshp_collector_amount = building_structure[
            'Row Houses' + ' ' + '1919 - 1948'].hp_amount_collector
        row_houses_1949_1978_gshp_collector_amount = building_structure[
            'Row Houses' + ' ' + '1949 - 1978'].hp_amount_collector
        row_houses_1979_1986_gshp_collector_amount = building_structure[
            'Row Houses' + ' ' + '1979 - 1986'].hp_amount_collector
        row_houses_1987_1990_gshp_collector_amount = building_structure[
            'Row Houses' + ' ' + '1987 - 1990'].hp_amount_collector
        row_houses_1991_1995_gshp_collector_amount = building_structure[
            'Row Houses' + ' ' + '1991 - 1995'].hp_amount_collector
        row_houses_1996_2000_gshp_collector_amount = building_structure[
            'Row Houses' + ' ' + '1996 - 2000'].hp_amount_collector
        row_houses_2001_2011_gshp_collector_amount = building_structure[
            'Row Houses' + ' ' + '2001 - 2011'].hp_amount_collector
        row_houses_2012_2022_gshp_collector_amount = building_structure[
            'Row Houses' + ' ' + '2012 - 2022'].hp_amount_collector
        row_houses_2023_2030_gshp_collector_amount = building_structure[
            'Row Houses' + ' ' + '2023 - 2030'].hp_amount_collector
        semi_detached_houses_beginn_1918_gshp_collector_amount = building_structure[
            'Semi-detached Houses' + ' ' + 'Before 1919'].hp_amount_collector
        semi_detached_houses_1919_1948_gshp_collector_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1919 - 1948'].hp_amount_collector
        semi_detached_houses_1949_1978_gshp_collector_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1949 - 1978'].hp_amount_collector
        semi_detached_houses_1979_1986_gshp_collector_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1979 - 1986'].hp_amount_collector
        semi_detached_houses_1987_1990_gshp_collector_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1987 - 1990'].hp_amount_collector
        semi_detached_houses_1991_1995_gshp_collector_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1991 - 1995'].hp_amount_collector
        semi_detached_houses_1996_2000_gshp_collector_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1996 - 2000'].hp_amount_collector
        semi_detached_houses_2001_2011_gshp_collector_amount = building_structure[
            'Semi-detached Houses' + ' ' + '2001 - 2011'].hp_amount_collector
        semi_detached_houses_2012_2022_gshp_collector_amount = building_structure[
            'Semi-detached Houses' + ' ' + '2012 - 2022'].hp_amount_collector
        semi_detached_houses_2023_2030_gshp_collector_amount = building_structure[
            'Semi-detached Houses' + ' ' + '2023 - 2030'].hp_amount_collector
        apartment_buildings_3_6_beginn_1918_gshp_collector_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + 'Before 1919'].hp_amount_collector
        apartment_buildings_3_6_1919_1948_gshp_collector_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1919 - 1948'].hp_amount_collector
        apartment_buildings_3_6_1949_1978_gshp_collector_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1949 - 1978'].hp_amount_collector
        apartment_buildings_3_6_1979_1986_gshp_collector_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1979 - 1986'].hp_amount_collector
        apartment_buildings_3_6_1987_1990_gshp_collector_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1987 - 1990'].hp_amount_collector
        apartment_buildings_3_6_1991_1995_gshp_collector_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1991 - 1995'].hp_amount_collector
        apartment_buildings_3_6_1996_2000_gshp_collector_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1996 - 2000'].hp_amount_collector
        apartment_buildings_3_6_2001_2011_gshp_collector_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '2001 - 2011'].hp_amount_collector
        apartment_buildings_3_6_2012_2022_gshp_collector_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '2012 - 2022'].hp_amount_collector
        apartment_buildings_3_6_2023_2030_gshp_collector_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '2023 - 2030'].hp_amount_collector
        apartment_buildings_7_more_beginn_1918_gshp_collector_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + 'Before 1919'].hp_amount_collector
        apartment_buildings_7_more_1919_1948_gshp_collector_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1919 - 1948'].hp_amount_collector
        apartment_buildings_7_more_1949_1978_gshp_collector_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1949 - 1978'].hp_amount_collector
        apartment_buildings_7_more_1979_1986_gshp_collector_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1979 - 1986'].hp_amount_collector
        apartment_buildings_7_more_1987_1990_gshp_collector_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1987 - 1990'].hp_amount_collector
        apartment_buildings_7_more_1991_1995_gshp_collector_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1991 - 1995'].hp_amount_collector
        apartment_buildings_7_more_1996_2000_gshp_collector_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1996 - 2000'].hp_amount_collector
        apartment_buildings_7_more_2001_2011_gshp_collector_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '2001 - 2011'].hp_amount_collector
        apartment_buildings_7_more_2012_2022_gshp_collector_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '2012 - 2022'].hp_amount_collector
        apartment_buildings_7_more_2023_2030_gshp_collector_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '2023 - 2030'].hp_amount_collector

        # gshp probe
        one_and_two_family_houses_beginn_1918_gshp_probe_amount = building_structure[
            'One- and Two-family Houses' + ' ' + 'Before 1919'].hp_amount_probe
        one_and_two_family_houses_1919_1948_gshp_probe_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1919 - 1948'].hp_amount_probe
        one_and_two_family_houses_1949_1978_gshp_probe_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1949 - 1978'].hp_amount_probe
        one_and_two_family_houses_1979_1986_gshp_probe_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1979 - 1986'].hp_amount_probe
        one_and_two_family_houses_1987_1990_gshp_probe_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1987 - 1990'].hp_amount_probe
        one_and_two_family_houses_1991_1995_gshp_probe_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1991 - 1995'].hp_amount_probe
        one_and_two_family_houses_1996_2000_gshp_probe_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '1996 - 2000'].hp_amount_probe
        one_and_two_family_houses_2001_2011_gshp_probe_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '2001 - 2011'].hp_amount_probe
        one_and_two_family_houses_2012_2022_gshp_probe_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '2012 - 2022'].hp_amount_probe
        one_and_two_family_houses_2023_2030_gshp_probe_amount = building_structure[
            'One- and Two-family Houses' + ' ' + '2023 - 2030'].hp_amount_probe
        row_houses_beginn_1918_gshp_probe_amount = building_structure[
            'Row Houses' + ' ' + 'Before 1919'].hp_amount_probe
        row_houses_1919_1948_gshp_probe_amount = building_structure[
            'Row Houses' + ' ' + '1919 - 1948'].hp_amount_probe
        row_houses_1949_1978_gshp_probe_amount = building_structure[
            'Row Houses' + ' ' + '1949 - 1978'].hp_amount_probe
        row_houses_1979_1986_gshp_probe_amount = building_structure[
            'Row Houses' + ' ' + '1979 - 1986'].hp_amount_probe
        row_houses_1987_1990_gshp_probe_amount = building_structure[
            'Row Houses' + ' ' + '1987 - 1990'].hp_amount_probe
        row_houses_1991_1995_gshp_probe_amount = building_structure[
            'Row Houses' + ' ' + '1991 - 1995'].hp_amount_probe
        row_houses_1996_2000_gshp_probe_amount = building_structure[
            'Row Houses' + ' ' + '1996 - 2000'].hp_amount_probe
        row_houses_2001_2011_gshp_probe_amount = building_structure[
            'Row Houses' + ' ' + '2001 - 2011'].hp_amount_probe
        row_houses_2012_2022_gshp_probe_amount = building_structure[
            'Row Houses' + ' ' + '2012 - 2022'].hp_amount_probe
        row_houses_2023_2030_gshp_probe_amount = building_structure[
            'Row Houses' + ' ' + '2023 - 2030'].hp_amount_probe
        semi_detached_houses_beginn_1918_gshp_probe_amount = building_structure[
            'Semi-detached Houses' + ' ' + 'Before 1919'].hp_amount_probe
        semi_detached_houses_1919_1948_gshp_probe_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1919 - 1948'].hp_amount_probe
        semi_detached_houses_1949_1978_gshp_probe_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1949 - 1978'].hp_amount_probe
        semi_detached_houses_1979_1986_gshp_probe_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1979 - 1986'].hp_amount_probe
        semi_detached_houses_1987_1990_gshp_probe_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1987 - 1990'].hp_amount_probe
        semi_detached_houses_1991_1995_gshp_probe_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1991 - 1995'].hp_amount_probe
        semi_detached_houses_1996_2000_gshp_probe_amount = building_structure[
            'Semi-detached Houses' + ' ' + '1996 - 2000'].hp_amount_probe
        semi_detached_houses_2001_2011_gshp_probe_amount = building_structure[
            'Semi-detached Houses' + ' ' + '2001 - 2011'].hp_amount_probe
        semi_detached_houses_2012_2022_gshp_probe_amount = building_structure[
            'Semi-detached Houses' + ' ' + '2012 - 2022'].hp_amount_probe
        semi_detached_houses_2023_2030_gshp_probe_amount = building_structure[
            'Semi-detached Houses' + ' ' + '2023 - 2030'].hp_amount_probe
        apartment_buildings_3_6_beginn_1918_gshp_probe_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + 'Before 1919'].hp_amount_probe
        apartment_buildings_3_6_1919_1948_gshp_probe_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1919 - 1948'].hp_amount_probe
        apartment_buildings_3_6_1949_1978_gshp_probe_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1949 - 1978'].hp_amount_probe
        apartment_buildings_3_6_1979_1986_gshp_probe_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1979 - 1986'].hp_amount_probe
        apartment_buildings_3_6_1987_1990_gshp_probe_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1987 - 1990'].hp_amount_probe
        apartment_buildings_3_6_1991_1995_gshp_probe_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1991 - 1995'].hp_amount_probe
        apartment_buildings_3_6_1996_2000_gshp_probe_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '1996 - 2000'].hp_amount_probe
        apartment_buildings_3_6_2001_2011_gshp_probe_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '2001 - 2011'].hp_amount_probe
        apartment_buildings_3_6_2012_2022_gshp_probe_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '2012 - 2022'].hp_amount_probe
        apartment_buildings_3_6_2023_2030_gshp_probe_amount = building_structure[
            'Apartment Buildings (3-6)' + ' ' + '2023 - 2030'].hp_amount_probe
        apartment_buildings_7_more_beginn_1918_gshp_probe_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + 'Before 1919'].hp_amount_probe
        apartment_buildings_7_more_1919_1948_gshp_probe_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1919 - 1948'].hp_amount_probe
        apartment_buildings_7_more_1949_1978_gshp_probe_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1949 - 1978'].hp_amount_probe
        apartment_buildings_7_more_1979_1986_gshp_probe_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1979 - 1986'].hp_amount_probe
        apartment_buildings_7_more_1987_1990_gshp_probe_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1987 - 1990'].hp_amount_probe
        apartment_buildings_7_more_1991_1995_gshp_probe_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1991 - 1995'].hp_amount_probe
        apartment_buildings_7_more_1996_2000_gshp_probe_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '1996 - 2000'].hp_amount_probe
        apartment_buildings_7_more_2001_2011_gshp_probe_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '2001 - 2011'].hp_amount_probe
        apartment_buildings_7_more_2012_2022_gshp_probe_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '2012 - 2022'].hp_amount_probe
        apartment_buildings_7_more_2023_2030_gshp_probe_amount = building_structure[
            'Apartment Buildings: 7 and More Apartments' + ' ' + '2023 - 2030'].hp_amount_probe

        for demand in electricity_demand_building_types:
            hourly_electricity_demand = 0

            # ashp
            hourly_electricity_demand += one_and_two_family_houses_beginn_1918_ashp_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_beginn_1918_ashp
            hourly_electricity_demand += one_and_two_family_houses_1919_1948_ashp_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1919_1948_ashp
            hourly_electricity_demand += one_and_two_family_houses_1949_1978_ashp_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1949_1978_ashp
            hourly_electricity_demand += one_and_two_family_houses_1979_1986_ashp_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1979_1986_ashp
            hourly_electricity_demand += one_and_two_family_houses_1987_1990_ashp_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1987_1990_ashp
            hourly_electricity_demand += one_and_two_family_houses_1991_1995_ashp_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1991_1995_ashp
            hourly_electricity_demand += one_and_two_family_houses_1996_2000_ashp_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1996_2000_ashp
            hourly_electricity_demand += one_and_two_family_houses_2001_2011_ashp_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_2001_2011_ashp
            hourly_electricity_demand += one_and_two_family_houses_2012_2022_ashp_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_2012_2022_ashp
            hourly_electricity_demand += one_and_two_family_houses_2023_2030_ashp_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_2023_2030_ashp
            hourly_electricity_demand += row_houses_beginn_1918_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_beginn_1918_ashp
            hourly_electricity_demand += row_houses_1919_1948_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1919_1948_ashp
            hourly_electricity_demand += row_houses_1949_1978_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1949_1978_ashp
            hourly_electricity_demand += row_houses_1979_1986_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1979_1986_ashp
            hourly_electricity_demand += row_houses_1987_1990_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1987_1990_ashp
            hourly_electricity_demand += row_houses_1991_1995_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1991_1995_ashp
            hourly_electricity_demand += row_houses_1996_2000_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1996_2000_ashp
            hourly_electricity_demand += row_houses_2001_2011_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2001_2011_ashp
            hourly_electricity_demand += row_houses_2012_2022_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2012_2022_ashp
            hourly_electricity_demand += row_houses_2023_2030_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2023_2030_ashp
            hourly_electricity_demand += semi_detached_houses_beginn_1918_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_beginn_1918_ashp
            hourly_electricity_demand += semi_detached_houses_1919_1948_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1919_1948_ashp
            hourly_electricity_demand += semi_detached_houses_1949_1978_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1949_1978_ashp
            hourly_electricity_demand += semi_detached_houses_1979_1986_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1979_1986_ashp
            hourly_electricity_demand += semi_detached_houses_1987_1990_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1987_1990_ashp
            hourly_electricity_demand += semi_detached_houses_1991_1995_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1991_1995_ashp
            hourly_electricity_demand += semi_detached_houses_1996_2000_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1996_2000_ashp
            hourly_electricity_demand += semi_detached_houses_2001_2011_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2001_2011_ashp
            hourly_electricity_demand += semi_detached_houses_2012_2022_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2012_2022_ashp
            hourly_electricity_demand += semi_detached_houses_2023_2030_ashp_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2023_2030_ashp
            hourly_electricity_demand += apartment_buildings_3_6_beginn_1918_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_beginn_1918_ashp
            hourly_electricity_demand += apartment_buildings_3_6_1919_1948_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1919_1948_ashp
            hourly_electricity_demand += apartment_buildings_3_6_1949_1978_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1949_1978_ashp
            hourly_electricity_demand += apartment_buildings_3_6_1979_1986_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1979_1986_ashp
            hourly_electricity_demand += apartment_buildings_3_6_1987_1990_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1987_1990_ashp
            hourly_electricity_demand += apartment_buildings_3_6_1991_1995_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1991_1995_ashp
            hourly_electricity_demand += apartment_buildings_3_6_1996_2000_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1996_2000_ashp
            hourly_electricity_demand += apartment_buildings_3_6_2001_2011_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_2001_2011_ashp
            hourly_electricity_demand += apartment_buildings_3_6_2012_2022_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_2012_2022_ashp
            hourly_electricity_demand += apartment_buildings_3_6_2023_2030_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_2023_2030_ashp
            hourly_electricity_demand += apartment_buildings_7_more_beginn_1918_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_beginn_1918_ashp
            hourly_electricity_demand += apartment_buildings_7_more_1919_1948_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1919_1948_ashp
            hourly_electricity_demand += apartment_buildings_7_more_1949_1978_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1949_1978_ashp
            hourly_electricity_demand += apartment_buildings_7_more_1979_1986_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1979_1986_ashp
            hourly_electricity_demand += apartment_buildings_7_more_1987_1990_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1987_1990_ashp
            hourly_electricity_demand += apartment_buildings_7_more_1991_1995_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1991_1995_ashp
            hourly_electricity_demand += apartment_buildings_7_more_1996_2000_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1996_2000_ashp
            hourly_electricity_demand += apartment_buildings_7_more_2001_2011_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_2001_2011_ashp
            hourly_electricity_demand += apartment_buildings_7_more_2012_2022_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_2012_2022_ashp
            hourly_electricity_demand += apartment_buildings_7_more_2023_2030_ashp_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_2023_2030_ashp

            # gshp collector
            hourly_electricity_demand += one_and_two_family_houses_beginn_1918_gshp_collector_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_beginn_1918_gshp_collector
            hourly_electricity_demand += one_and_two_family_houses_1919_1948_gshp_collector_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1919_1948_gshp_collector
            hourly_electricity_demand += one_and_two_family_houses_1949_1978_gshp_collector_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1949_1978_gshp_collector
            hourly_electricity_demand += one_and_two_family_houses_1979_1986_gshp_collector_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1979_1986_gshp_collector
            hourly_electricity_demand += one_and_two_family_houses_1987_1990_gshp_collector_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1987_1990_gshp_collector
            hourly_electricity_demand += one_and_two_family_houses_1991_1995_gshp_collector_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1991_1995_gshp_collector
            hourly_electricity_demand += one_and_two_family_houses_1996_2000_gshp_collector_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1996_2000_gshp_collector
            hourly_electricity_demand += one_and_two_family_houses_2001_2011_gshp_collector_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_2001_2011_gshp_collector
            hourly_electricity_demand += one_and_two_family_houses_2012_2022_gshp_collector_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_2012_2022_gshp_collector
            hourly_electricity_demand += one_and_two_family_houses_2023_2030_gshp_collector_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_2023_2030_gshp_collector
            hourly_electricity_demand += row_houses_beginn_1918_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_beginn_1918_gshp_collector
            hourly_electricity_demand += row_houses_1919_1948_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1919_1948_gshp_collector
            hourly_electricity_demand += row_houses_1949_1978_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1949_1978_gshp_collector
            hourly_electricity_demand += row_houses_1979_1986_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1979_1986_gshp_collector
            hourly_electricity_demand += row_houses_1987_1990_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1987_1990_gshp_collector
            hourly_electricity_demand += row_houses_1991_1995_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1991_1995_gshp_collector
            hourly_electricity_demand += row_houses_1996_2000_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1996_2000_gshp_collector
            hourly_electricity_demand += row_houses_2001_2011_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2001_2011_gshp_collector
            hourly_electricity_demand += row_houses_2012_2022_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2012_2022_gshp_collector
            hourly_electricity_demand += row_houses_2023_2030_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2023_2030_gshp_collector
            hourly_electricity_demand += semi_detached_houses_beginn_1918_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_beginn_1918_gshp_collector
            hourly_electricity_demand += semi_detached_houses_1919_1948_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1919_1948_gshp_collector
            hourly_electricity_demand += semi_detached_houses_1949_1978_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1949_1978_gshp_collector
            hourly_electricity_demand += semi_detached_houses_1979_1986_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1979_1986_gshp_collector
            hourly_electricity_demand += semi_detached_houses_1987_1990_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1987_1990_gshp_collector
            hourly_electricity_demand += semi_detached_houses_1991_1995_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1991_1995_gshp_collector
            hourly_electricity_demand += semi_detached_houses_1996_2000_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1996_2000_gshp_collector
            hourly_electricity_demand += semi_detached_houses_2001_2011_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2001_2011_gshp_collector
            hourly_electricity_demand += semi_detached_houses_2012_2022_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2012_2022_gshp_collector
            hourly_electricity_demand += semi_detached_houses_2023_2030_gshp_collector_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2023_2030_gshp_collector
            hourly_electricity_demand += apartment_buildings_3_6_beginn_1918_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_beginn_1918_gshp_collector
            hourly_electricity_demand += apartment_buildings_3_6_1919_1948_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1919_1948_gshp_collector
            hourly_electricity_demand += apartment_buildings_3_6_1949_1978_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1949_1978_gshp_collector
            hourly_electricity_demand += apartment_buildings_3_6_1979_1986_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1979_1986_gshp_collector
            hourly_electricity_demand += apartment_buildings_3_6_1987_1990_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1987_1990_gshp_collector
            hourly_electricity_demand += apartment_buildings_3_6_1991_1995_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1991_1995_gshp_collector
            hourly_electricity_demand += apartment_buildings_3_6_1996_2000_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1996_2000_gshp_collector
            hourly_electricity_demand += apartment_buildings_3_6_2001_2011_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_2001_2011_gshp_collector
            hourly_electricity_demand += apartment_buildings_3_6_2012_2022_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_2012_2022_gshp_collector
            hourly_electricity_demand += apartment_buildings_3_6_2023_2030_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_2023_2030_gshp_collector
            hourly_electricity_demand += apartment_buildings_7_more_beginn_1918_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_beginn_1918_gshp_collector
            hourly_electricity_demand += apartment_buildings_7_more_1919_1948_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1919_1948_gshp_collector
            hourly_electricity_demand += apartment_buildings_7_more_1949_1978_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1949_1978_gshp_collector
            hourly_electricity_demand += apartment_buildings_7_more_1979_1986_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1979_1986_gshp_collector
            hourly_electricity_demand += apartment_buildings_7_more_1987_1990_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1987_1990_gshp_collector
            hourly_electricity_demand += apartment_buildings_7_more_1991_1995_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1991_1995_gshp_collector
            hourly_electricity_demand += apartment_buildings_7_more_1996_2000_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1996_2000_gshp_collector
            hourly_electricity_demand += apartment_buildings_7_more_2001_2011_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_2001_2011_gshp_collector
            hourly_electricity_demand += apartment_buildings_7_more_2012_2022_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_2012_2022_gshp_collector
            hourly_electricity_demand += apartment_buildings_7_more_2023_2030_gshp_collector_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_2023_2030_gshp_collector

            # gshp probe
            hourly_electricity_demand += one_and_two_family_houses_beginn_1918_gshp_probe_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_beginn_1918_gshp_probe
            hourly_electricity_demand += one_and_two_family_houses_1919_1948_gshp_probe_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1919_1948_gshp_probe
            hourly_electricity_demand += one_and_two_family_houses_1949_1978_gshp_probe_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1949_1978_gshp_probe
            hourly_electricity_demand += one_and_two_family_houses_1979_1986_gshp_probe_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1979_1986_gshp_probe
            hourly_electricity_demand += one_and_two_family_houses_1987_1990_gshp_probe_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1987_1990_gshp_probe
            hourly_electricity_demand += one_and_two_family_houses_1991_1995_gshp_probe_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1991_1995_gshp_probe
            hourly_electricity_demand += one_and_two_family_houses_1996_2000_gshp_probe_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_1996_2000_gshp_probe
            hourly_electricity_demand += one_and_two_family_houses_2001_2011_gshp_probe_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_2001_2011_gshp_probe
            hourly_electricity_demand += one_and_two_family_houses_2012_2022_gshp_probe_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_2012_2022_gshp_probe
            hourly_electricity_demand += one_and_two_family_houses_2023_2030_gshp_probe_amount * \
                electricity_demand_building_types[demand].one_and_two_family_houses_2023_2030_gshp_probe
            hourly_electricity_demand += row_houses_beginn_1918_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_beginn_1918_gshp_probe
            hourly_electricity_demand += row_houses_1919_1948_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1919_1948_gshp_probe
            hourly_electricity_demand += row_houses_1949_1978_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1949_1978_gshp_probe
            hourly_electricity_demand += row_houses_1979_1986_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1979_1986_gshp_probe
            hourly_electricity_demand += row_houses_1987_1990_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1987_1990_gshp_probe
            hourly_electricity_demand += row_houses_1991_1995_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1991_1995_gshp_probe
            hourly_electricity_demand += row_houses_1996_2000_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1996_2000_gshp_probe
            hourly_electricity_demand += row_houses_2001_2011_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2001_2011_gshp_probe
            hourly_electricity_demand += row_houses_2012_2022_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2012_2022_gshp_probe
            hourly_electricity_demand += row_houses_2023_2030_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2023_2030_gshp_probe
            hourly_electricity_demand += semi_detached_houses_beginn_1918_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_beginn_1918_gshp_probe
            hourly_electricity_demand += semi_detached_houses_1919_1948_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1919_1948_gshp_probe
            hourly_electricity_demand += semi_detached_houses_1949_1978_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1949_1978_gshp_probe
            hourly_electricity_demand += semi_detached_houses_1979_1986_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1979_1986_gshp_probe
            hourly_electricity_demand += semi_detached_houses_1987_1990_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1987_1990_gshp_probe
            hourly_electricity_demand += semi_detached_houses_1991_1995_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1991_1995_gshp_probe
            hourly_electricity_demand += semi_detached_houses_1996_2000_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_1996_2000_gshp_probe
            hourly_electricity_demand += semi_detached_houses_2001_2011_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2001_2011_gshp_probe
            hourly_electricity_demand += semi_detached_houses_2012_2022_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2012_2022_gshp_probe
            hourly_electricity_demand += semi_detached_houses_2023_2030_gshp_probe_amount * \
                electricity_demand_building_types[demand].row_and_semi_detached_houses_2023_2030_gshp_probe
            hourly_electricity_demand += apartment_buildings_3_6_beginn_1918_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_beginn_1918_gshp_probe
            hourly_electricity_demand += apartment_buildings_3_6_1919_1948_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1919_1948_gshp_probe
            hourly_electricity_demand += apartment_buildings_3_6_1949_1978_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1949_1978_gshp_probe
            hourly_electricity_demand += apartment_buildings_3_6_1979_1986_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1979_1986_gshp_probe
            hourly_electricity_demand += apartment_buildings_3_6_1987_1990_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1987_1990_gshp_probe
            hourly_electricity_demand += apartment_buildings_3_6_1991_1995_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1991_1995_gshp_probe
            hourly_electricity_demand += apartment_buildings_3_6_1996_2000_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_1996_2000_gshp_probe
            hourly_electricity_demand += apartment_buildings_3_6_2001_2011_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_2001_2011_gshp_probe
            hourly_electricity_demand += apartment_buildings_3_6_2012_2022_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_2012_2022_gshp_probe
            hourly_electricity_demand += apartment_buildings_3_6_2023_2030_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_3_6_2023_2030_gshp_probe
            hourly_electricity_demand += apartment_buildings_7_more_beginn_1918_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_beginn_1918_gshp_probe
            hourly_electricity_demand += apartment_buildings_7_more_1919_1948_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1919_1948_gshp_probe
            hourly_electricity_demand += apartment_buildings_7_more_1949_1978_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1949_1978_gshp_probe
            hourly_electricity_demand += apartment_buildings_7_more_1979_1986_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1979_1986_gshp_probe
            hourly_electricity_demand += apartment_buildings_7_more_1987_1990_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1987_1990_gshp_probe
            hourly_electricity_demand += apartment_buildings_7_more_1991_1995_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1991_1995_gshp_probe
            hourly_electricity_demand += apartment_buildings_7_more_1996_2000_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_1996_2000_gshp_probe
            hourly_electricity_demand += apartment_buildings_7_more_2001_2011_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_2001_2011_gshp_probe
            hourly_electricity_demand += apartment_buildings_7_more_2012_2022_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_2012_2022_gshp_probe
            hourly_electricity_demand += apartment_buildings_7_more_2023_2030_gshp_probe_amount * \
                electricity_demand_building_types[demand].apartment_buildings_7_more_2023_2030_gshp_probe

            electricity_demand[demand] = HourlyElectricityDemand(
                nuts3_code=region,
                time=electricity_demand_building_types[demand].time,
                hourly_electricity_demand=hourly_electricity_demand)

        regions_electricity_demand.regions[region] = electricity_demand
        print(region)

    return regions_electricity_demand


def calculate_regions_electricity_demand(
        regions_electricity_demand: RegionsElectricityDemand,
        electricity_demand_path: ElectricityDemandPath
) -> RegionsElectricityDemand:

    combined_building_structure = get_building_structure()

    get_hourly_electricity_demand(
        regions_electricity_demand=regions_electricity_demand,
        electricity_demand_path=electricity_demand_path,
        combined_building_structure=combined_building_structure
    )

    return regions_electricity_demand
