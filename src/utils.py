import csv
from src.classes import RegionInfo, BuildingInfo


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


class BuildingInfoReader:
    def __call__(self, file_path) -> dict[str, list[BuildingInfo]]:
        combined_building_info: dict[str, list[BuildingInfo]] = dict()

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
                    if combined_building_info.get(nuts3_code, -1) == -1:
                        combined_building_info[nuts3_code] = list()
                        combined_building_info[nuts3_code].append(buildin_info)
                    else:
                        combined_building_info[nuts3_code].append(buildin_info)
                line_count += 1

        return combined_building_info


class CsvReader:
    def __init__(self, reader_type) -> None:
        self.reader_type = reader_type

    def read(self, file_path):
        return self.reader_type(file_path)
