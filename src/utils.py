import csv
from src.classes import RegionInfo


class RegionInfoReader:
    def __call__(self, file_path) -> list[RegionInfo]:
        print("Reading csv")
        combined_region_infos = []
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    combined_region_infos.append(
                        RegionInfo(
                            row[0],
                            row[1],
                            row[2],
                            row[3],
                            row[4],
                            row[5],
                            row[6]
                        )
                    )
                line_count += 1
            print(f'Processed {line_count} lines.')
        return combined_region_infos


class CsvReader:
    def __init__(self, reader_type) -> None:
        self.reader_type = reader_type

    def read(self, file_path):
        return self.reader_type(file_path)
