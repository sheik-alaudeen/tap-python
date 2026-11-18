import csv
from pathlib import Path

def read_csv(path: Path) -> list[dict]:
    """
    Read a CSV file and return records as a list of dictionaries.
    """

    with open(path, 'r', encoding='utf-8', newline='') as file:
        sample = file.read(2048)
        file.seek(0)

        dialect = csv.Sniffer().sniff(sample, delimiters=',;')
        reader = csv.DictReader(file, dialect=dialect)

        data = list(reader)

    return data