# Напишите функцию, которая получает на вход директорию и рекурсивно обходит
# её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# * Для дочерних объектов указывайте родительскую директорию.
# * Для каждого объекта укажите файл это или директория.
# * Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом
# всех вложенных файлов и директорий.

import json
import csv
import pickle
import convert_dict_to_json
import convert_dict_to_csv
import convert_dict_to_pickle
from pathlib import Path


def catalogs_walk(data: Path) -> dict[str, list]:
    paths = sorted(Path('Test').rglob('*'))

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
