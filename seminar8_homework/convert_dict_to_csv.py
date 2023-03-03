import csv


def convert_to_csv(data: dict) -> None:
    rows = []
    for k, v in data.items():
        rows.append({k: v})

    with open('result.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['directory', 'files', 'name', 'parent', 'size']

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
