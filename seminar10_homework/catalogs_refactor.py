import csv
import json
import pickle
from pathlib import Path


class Catalogs:

    def __init__(self, directory: Path):
        self.catalog = directory

    def catalogs_walk(self) -> dict[str, list]:
        paths = sorted(self.catalog.rglob('*'))

        my_dict = {
            'directory': None,
            'files': None
        }
        files_lst = []
        folders_lst = []
        count = 0
        for p in paths:

            if p.is_file():
                files_lst.extend(list((p.name, str(p.parent), p.stat().st_size)))

            elif p.is_dir():
                count += sum(file.stat().st_size for file in paths if file.is_file())
                folders_lst.extend(list((p.name, str(p.parent), count)))

        my_dict['files'] = files_lst
        my_dict['directory'] = folders_lst

        return my_dict

    @staticmethod
    def convert_to_json(data: dict) -> None:
        with open('result.json', 'w') as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def convert_to_csv(data: dict) -> None:
        rows = []
        for k, v in data.items():
            rows.append({k: v})

        with open('result.csv', 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['directory', 'files', 'name', 'parent', 'size']

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    @staticmethod
    def convert_to_pickle(data: dict) -> None:
        with open('result.pickle', 'wb') as f:
            pickle.dump(data, f)


if __name__ == '__main__':
    path = Path('Test')
    obj = Catalogs(path)
    obj.catalogs_walk()
    obj.convert_to_json(obj.catalogs_walk())
    obj.convert_to_csv(obj.catalogs_walk())
    obj.convert_to_pickle(obj.catalogs_walk())
