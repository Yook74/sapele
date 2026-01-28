import csv
import pandas as pd
from datetime import datetime
import data_storage as store_to_file
import datetime
from typing import Iterable
import os


file_path = r'C:\\Users\carl.young\Documents\sapele\csv_stuff\my_orders.csv'
csv_labels = ['Name', 'Type', 'Key', 'Octave', 'Ref', 'Scale', 'Flute', 'Block', 'Qty', 'Price',
              'Total', 'Order_Date', 'Ship_Date']
orders = pd.read_csv(file_path)
pd.set_option('display.max_columns', None)


def view_orders():
    print()
    print(orders.to_string(index=False, justify='center'))
    input('\nPress Enter to continue...')


def take_order():
    order = []
    key = ''
    flute_wood = ''
    block_wood = ''
    price = 0

    order.append(len(orders)+1)
    print()

    first_name = input('First Name: ')
    while not first_name:
        first_name = input('First Name: ')
    last_name = input('Last Name: ')
    while not last_name:
        last_name = input('Last Name: ')
    name = f'{first_name}_{last_name}'
    order.append(name)
    flute_type = input('Flute Type: (1) Single, (2) Drone) ')
    while not flute_type:
        flute_type = input('Flute Type: (1) Single, (2) Drone) ')
    order.append(flute_type)

    while not key:
        key = input('Key: ')
    order.append(key)

    octave = input('Octave: (4) ')
    if not octave:
        octave = '4'
    order.append(octave)

    ref = input('Tuning Ref: (440) ')
    if not ref:
        ref = '440'
    order.append(ref)

    scale = input('Scale (Minor Pent): ')
    if not scale:
        scale = 'Minor_Pent'
    order.append(scale)

    while not flute_wood:
        flute_wood = input('Flute Wood: ')
    order.append(flute_wood)

    while not block_wood:
        block_wood = input('Block Wood: ')
    order.append(block_wood)

    qty = input('Qty: (1) ')
    if not qty:
        qty = 1
    order.append(qty)

    while not price:
        price = input('Price: ')
    order.append(float(price))

    total = float(price) * int(qty)
    order.append(total)

    order_date = input('Order Date (today): ')
    if not order_date:
        order_date = f'{datetime.date.today().month}/{datetime.date.today().day}/{datetime.date.today().year}'
    order.append(order_date)

    ship_date = input('Ship Date: ')
    if not ship_date:
        ship_date = 'Not_Shipped'
    order.append(ship_date)

    store_to_file.append_to_csv(file_path, order)
    print(order)


def update_order():
    num = 1
    names = []
    print()
    with open(file_path, 'r') as csv_file:
        csv_reader: Iterable[dict[str, str]] = csv.DictReader(csv_file)
        for row in csv_reader:
            print(f"{num}: {row.get('Order ID')}, {row.get('Name')}, {row.get('Flute Type')}, {row.get('Key')}, "
                  f"{row.get('Octave')}, {row.get('REF')}, {row.get('Scale')}, {row.get('Flute Wood')}, "
                  f"{row.get('Block Wood')}, {row.get('Qty')}, {row.get('Price')}, {row.get('Total Price')}, "
                  f"{row.get('Order Date')}, {row.get('Ship Date')}")
            num += 1
            names.append(row.get('Name'))
        order_id = input('\nSelect Order ID: \n')
        while not order_id:
            order_id = input('\nSelect Order ID: \n')
        num = 0
        with open(file_path, 'r') as csv_file:
            csv_reader: Iterable[dict[str, str]] = csv.DictReader(csv_file)
            for row in csv_reader:
                if int(row.get('Order_ID')) == int(order_id):
                    row_data = list(row.items())
                    for item in row_data:
                        print(f'{num}. {item}')
                        num += 1
                    item_num = input('\nSelect Item: ')
                    while item_num:
                        column_name = row_data[int(item_num)][0]
                        new_value = input('Enter replacement value: ')
                        store_to_file.update_file(file_path, 'Order_ID', order_id, column_name, new_value)


def view_customer_orders():
    num = 1
    print()
    with open(file_path, 'r') as csv_file:
        csv_reader: Iterable[dict[str, str]] = csv.DictReader(csv_file)
        ref = []
        for row in csv_reader:
            if row.get('Name') not in ref:
                print(f"{num}: {row.get('Name')}")
                ref.append(row.get('Name'))
                num += 1
        select = input('\nSelect Name: ')
        while not select:
            select = input('\nSelect Name: ')
        name = ref[int(select)-1]
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print(orders[orders['Name'].str.contains(name)].to_string(index=False, justify='center'))

    input('\nPress Enter to continue...')
