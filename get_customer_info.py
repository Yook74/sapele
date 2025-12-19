import csv
from typing import Iterable


def get_customer(settings_path, column_name, row_select):
    rows = []
    with open(settings_path, 'r') as csv_file:

        csv_reader: Iterable[dict[str, str]] = csv.DictReader(csv_file)
        for row in csv_reader:
            # if row[column_name] == row_select:
            rows.append(row)
    return rows

def add_customer():
    print()


if __name__ == '__main__':
    row = get_customer(r'/New Sapele/csv stuff/customer.csv', 'First Name', 'Craig')
    num = 1
    for data in row:
        customer = f'\n{num}: {data["Name"]}, {data["Address"]}, ' \
                   f'{data["City"]}, {data["State"]}, {data["Postal Code"]}, {data["Country"]}'
        num += 1
        print(customer)
