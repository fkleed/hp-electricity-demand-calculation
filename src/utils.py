import csv
import json
import dataclasses
from src.classes import RegionInfo, BuildingInfo, ElectricityDemand


class RegionInfoReader:
    def __call__(self, file_path) -> list[RegionInfo]:
        combined_region_infos: list[RegionInfo] = []

        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    combined_region_infos.append(
                        RegionInfo(
                            nuts1_code=row[0],
                            nuts1_name=row[1],
                            nuts2_code=row[2],
                            nuts2_name=row[3],
                            nuts3_code=row[4],
                            nuts3_name=row[5],
                            nuts3_type=row[6]
                        )
                    )
                line_count += 1

        return combined_region_infos


class BuildingStructureReader:
    def __call__(self, file_path) -> dict[str, dict[str, BuildingInfo]]:
        combined_building_structure: dict[str,
                                          dict[str, BuildingInfo]] = dict()

        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    nuts3_code = row[0]
                    buildin_info = BuildingInfo(
                        building_type_size=row[1],
                        year_of_construction=row[2],
                        building_count=int(row[3]),
                        hp_potential_total=float(row[4]),
                        hp_potential_air=float(row[5]),
                        hp_potential_probe=float(row[6]),
                        hp_potential_collector=float(row[7]),
                        hp_amount_air=float(row[8]),
                        hp_amount_probe=float(row[9]),
                        hp_amount_collector=float(row[10])
                    )
                    if combined_building_structure.get(nuts3_code, -1) == -1:
                        combined_building_structure[nuts3_code] = dict()
                        combined_building_structure[nuts3_code][buildin_info.building_type_size + ' ' +
                                                                buildin_info.year_of_construction] = buildin_info
                    else:
                        combined_building_structure[nuts3_code][buildin_info.building_type_size + ' ' +
                                                                buildin_info.year_of_construction] = buildin_info
                line_count += 1

        return combined_building_structure


class ElectricityDemandReader:
    def __call__(self, file_path) -> dict[str, ElectricityDemand]:
        electricity_demand: dict[str, ElectricityDemand] = dict()

        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    time = row[0]
                    electricity_demand[time] = ElectricityDemand(
                        time=time,
                        temperature_kelvin=float(row[1]),
                        soil_temperature_kelvin_collector=float(row[2]),
                        soil_temperature_kelvin_probe=float(row[3]),
                        one_and_two_family_houses_beginn_1918_ashp=float(
                            row[4]),
                        one_and_two_family_houses_1919_1948_ashp=float(row[5]),
                        one_and_two_family_houses_1949_1978_ashp=float(row[6]),
                        one_and_two_family_houses_1979_1986_ashp=float(row[7]),
                        one_and_two_family_houses_1987_1990_ashp=float(row[8]),
                        one_and_two_family_houses_1991_1995_ashp=float(row[9]),
                        one_and_two_family_houses_1996_2000_ashp=float(
                            row[10]),
                        one_and_two_family_houses_2001_2011_ashp=float(
                            row[11]),
                        one_and_two_family_houses_2012_2022_ashp=float(
                            row[12]),
                        one_and_two_family_houses_2023_2030_ashp=float(
                            row[13]),
                        row_and_semi_detached_houses_beginn_1918_ashp=float(
                            row[14]),
                        row_and_semi_detached_houses_1919_1948_ashp=float(
                            row[15]),
                        row_and_semi_detached_houses_1949_1978_ashp=float(
                            row[16]),
                        row_and_semi_detached_houses_1979_1986_ashp=float(
                            row[17]),
                        row_and_semi_detached_houses_1987_1990_ashp=float(
                            row[18]),
                        row_and_semi_detached_houses_1991_1995_ashp=float(
                            row[19]),
                        row_and_semi_detached_houses_1996_2000_ashp=float(
                            row[20]),
                        row_and_semi_detached_houses_2001_2011_ashp=float(
                            row[21]),
                        row_and_semi_detached_houses_2012_2022_ashp=float(
                            row[22]),
                        row_and_semi_detached_houses_2023_2030_ashp=float(
                            row[23]),
                        apartment_buildings_3_6_beginn_1918_ashp=float(
                            row[24]),
                        apartment_buildings_3_6_1919_1948_ashp=float(row[25]),
                        apartment_buildings_3_6_1949_1978_ashp=float(row[26]),
                        apartment_buildings_3_6_1979_1986_ashp=float(row[27]),
                        apartment_buildings_3_6_1987_1990_ashp=float(row[28]),
                        apartment_buildings_3_6_1991_1995_ashp=float(row[29]),
                        apartment_buildings_3_6_1996_2000_ashp=float(row[30]),
                        apartment_buildings_3_6_2001_2011_ashp=float(row[31]),
                        apartment_buildings_3_6_2012_2022_ashp=float(row[32]),
                        apartment_buildings_3_6_2023_2030_ashp=float(row[33]),
                        apartment_buildings_7_more_beginn_1918_ashp=float(
                            row[34]),
                        apartment_buildings_7_more_1919_1948_ashp=float(
                            row[35]),
                        apartment_buildings_7_more_1949_1978_ashp=float(
                            row[36]),
                        apartment_buildings_7_more_1979_1986_ashp=float(
                            row[37]),
                        apartment_buildings_7_more_1987_1990_ashp=float(
                            row[38]),
                        apartment_buildings_7_more_1991_1995_ashp=float(
                            row[39]),
                        apartment_buildings_7_more_1996_2000_ashp=float(
                            row[40]),
                        apartment_buildings_7_more_2001_2011_ashp=float(
                            row[41]),
                        apartment_buildings_7_more_2012_2022_ashp=float(
                            row[42]),
                        apartment_buildings_7_more_2023_2030_ashp=float(
                            row[43]),
                        one_and_two_family_houses_beginn_1918_gshp_collector=float(
                            row[44]),
                        one_and_two_family_houses_1919_1948_gshp_collector=float(
                            row[45]),
                        one_and_two_family_houses_1949_1978_gshp_collector=float(
                            row[46]),
                        one_and_two_family_houses_1979_1986_gshp_collector=float(
                            row[47]),
                        one_and_two_family_houses_1987_1990_gshp_collector=float(
                            row[48]),
                        one_and_two_family_houses_1991_1995_gshp_collector=float(
                            row[49]),
                        one_and_two_family_houses_1996_2000_gshp_collector=float(
                            row[50]),
                        one_and_two_family_houses_2001_2011_gshp_collector=float(
                            row[51]),
                        one_and_two_family_houses_2012_2022_gshp_collector=float(
                            row[52]),
                        one_and_two_family_houses_2023_2030_gshp_collector=float(
                            row[53]),
                        row_and_semi_detached_houses_beginn_1918_gshp_collector=float(
                            row[54]),
                        row_and_semi_detached_houses_1919_1948_gshp_collector=float(
                            row[55]),
                        row_and_semi_detached_houses_1949_1978_gshp_collector=float(
                            row[56]),
                        row_and_semi_detached_houses_1979_1986_gshp_collector=float(
                            row[57]),
                        row_and_semi_detached_houses_1987_1990_gshp_collector=float(
                            row[58]),
                        row_and_semi_detached_houses_1991_1995_gshp_collector=float(
                            row[59]),
                        row_and_semi_detached_houses_1996_2000_gshp_collector=float(
                            row[60]),
                        row_and_semi_detached_houses_2001_2011_gshp_collector=float(
                            row[61]),
                        row_and_semi_detached_houses_2012_2022_gshp_collector=float(
                            row[62]),
                        row_and_semi_detached_houses_2023_2030_gshp_collector=float(
                            row[63]),
                        apartment_buildings_3_6_beginn_1918_gshp_collector=float(
                            row[64]),
                        apartment_buildings_3_6_1919_1948_gshp_collector=float(
                            row[65]),
                        apartment_buildings_3_6_1949_1978_gshp_collector=float(
                            row[66]),
                        apartment_buildings_3_6_1979_1986_gshp_collector=float(
                            row[67]),
                        apartment_buildings_3_6_1987_1990_gshp_collector=float(
                            row[68]),
                        apartment_buildings_3_6_1991_1995_gshp_collector=float(
                            row[69]),
                        apartment_buildings_3_6_1996_2000_gshp_collector=float(
                            row[70]),
                        apartment_buildings_3_6_2001_2011_gshp_collector=float(
                            row[71]),
                        apartment_buildings_3_6_2012_2022_gshp_collector=float(
                            row[72]),
                        apartment_buildings_3_6_2023_2030_gshp_collector=float(
                            row[73]),
                        apartment_buildings_7_more_beginn_1918_gshp_collector=float(
                            row[74]),
                        apartment_buildings_7_more_1919_1948_gshp_collector=float(
                            row[75]),
                        apartment_buildings_7_more_1949_1978_gshp_collector=float(
                            row[76]),
                        apartment_buildings_7_more_1979_1986_gshp_collector=float(
                            row[77]),
                        apartment_buildings_7_more_1987_1990_gshp_collector=float(
                            row[78]),
                        apartment_buildings_7_more_1991_1995_gshp_collector=float(
                            row[79]),
                        apartment_buildings_7_more_1996_2000_gshp_collector=float(
                            row[80]),
                        apartment_buildings_7_more_2001_2011_gshp_collector=float(
                            row[81]),
                        apartment_buildings_7_more_2012_2022_gshp_collector=float(
                            row[82]),
                        apartment_buildings_7_more_2023_2030_gshp_collector=float(
                            row[83]),
                        one_and_two_family_houses_beginn_1918_gshp_probe=float(
                            row[84]),
                        one_and_two_family_houses_1919_1948_gshp_probe=float(
                            row[85]),
                        one_and_two_family_houses_1949_1978_gshp_probe=float(
                            row[86]),
                        one_and_two_family_houses_1979_1986_gshp_probe=float(
                            row[87]),
                        one_and_two_family_houses_1987_1990_gshp_probe=float(
                            row[88]),
                        one_and_two_family_houses_1991_1995_gshp_probe=float(
                            row[89]),
                        one_and_two_family_houses_1996_2000_gshp_probe=float(
                            row[90]),
                        one_and_two_family_houses_2001_2011_gshp_probe=float(
                            row[91]),
                        one_and_two_family_houses_2012_2022_gshp_probe=float(
                            row[92]),
                        one_and_two_family_houses_2023_2030_gshp_probe=float(
                            row[93]),
                        row_and_semi_detached_houses_beginn_1918_gshp_probe=float(
                            row[94]),
                        row_and_semi_detached_houses_1919_1948_gshp_probe=float(
                            row[95]),
                        row_and_semi_detached_houses_1949_1978_gshp_probe=float(
                            row[96]),
                        row_and_semi_detached_houses_1979_1986_gshp_probe=float(
                            row[97]),
                        row_and_semi_detached_houses_1987_1990_gshp_probe=float(
                            row[98]),
                        row_and_semi_detached_houses_1991_1995_gshp_probe=float(
                            row[99]),
                        row_and_semi_detached_houses_1996_2000_gshp_probe=float(
                            row[100]),
                        row_and_semi_detached_houses_2001_2011_gshp_probe=float(
                            row[101]),
                        row_and_semi_detached_houses_2012_2022_gshp_probe=float(
                            row[102]),
                        row_and_semi_detached_houses_2023_2030_gshp_probe=float(
                            row[103]),
                        apartment_buildings_3_6_beginn_1918_gshp_probe=float(
                            row[104]),
                        apartment_buildings_3_6_1919_1948_gshp_probe=float(
                            row[105]),
                        apartment_buildings_3_6_1949_1978_gshp_probe=float(
                            row[106]),
                        apartment_buildings_3_6_1979_1986_gshp_probe=float(
                            row[107]),
                        apartment_buildings_3_6_1987_1990_gshp_probe=float(
                            row[108]),
                        apartment_buildings_3_6_1991_1995_gshp_probe=float(
                            row[109]),
                        apartment_buildings_3_6_1996_2000_gshp_probe=float(
                            row[110]),
                        apartment_buildings_3_6_2001_2011_gshp_probe=float(
                            row[111]),
                        apartment_buildings_3_6_2012_2022_gshp_probe=float(
                            row[112]),
                        apartment_buildings_3_6_2023_2030_gshp_probe=float(
                            row[113]),
                        apartment_buildings_7_more_beginn_1918_gshp_probe=float(
                            row[114]),
                        apartment_buildings_7_more_1919_1948_gshp_probe=float(
                            row[115]),
                        apartment_buildings_7_more_1949_1978_gshp_probe=float(
                            row[116]),
                        apartment_buildings_7_more_1979_1986_gshp_probe=float(
                            row[117]),
                        apartment_buildings_7_more_1987_1990_gshp_probe=float(
                            row[118]),
                        apartment_buildings_7_more_1991_1995_gshp_probe=float(
                            row[119]),
                        apartment_buildings_7_more_1996_2000_gshp_probe=float(
                            row[120]),
                        apartment_buildings_7_more_2001_2011_gshp_probe=float(
                            row[121]),
                        apartment_buildings_7_more_2012_2022_gshp_probe=float(
                            row[122]),
                        apartment_buildings_7_more_2023_2030_gshp_probe=float(
                            row[123])
                    )
                line_count += 1

        return electricity_demand


class CsvReader:
    def __init__(self, reader_type):
        self.reader_type = reader_type

    def read(self, file_path):
        return self.reader_type(file_path)


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


class JsonSerializer:
    def __call__(self, data):
        return json.dumps(data, cls=EnhancedJSONEncoder)


class DataSerializer:
    def __init__(self, serializing_strategy):
        self.serializing_strategy = serializing_strategy

    def serialize(self, data):
        return self.serializing_strategy(data)
