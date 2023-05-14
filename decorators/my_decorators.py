import csv
import json
from typing import Callable


def decorator_data_to_json(func: Callable):
    def wrapper(*args, **kwargs):
        data = {}
        with open('result.json', 'a', encoding='utf-8') as f:
            key = str(func(*args, **kwargs)[0:1])
            value = str(func(*args, **kwargs)[1:])
            print(value)
            data[key] = value
            json.dump(data, f, indent=2)
            return data

    return wrapper


def decorator_data_from_csv(func: Callable):
    def wrapper(*args, **kwargs):
        with open('numbers.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            while True:
                for row in reader:
                    x, y, z = int(row[0]), int(row[1]), int(row[2])
                    result = func(x, y, z, *args, **kwargs)
                    print(result)

                return result, x, y, z

    return wrapper
