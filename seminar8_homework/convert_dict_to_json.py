import json


def convert_to_json(data: dict) -> None:
    with open('result.json', 'w') as f:
        json.dump(data, f, indent=2)