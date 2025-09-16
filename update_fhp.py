import csv
from database.models import FHP
from database.connection import get_session
from sqlalchemy import update
import numpy as np

sess = get_session()


def spacing(nums):
    for lines in range(nums):
        print()


def get_fhp_values(key, octave):
    item_list = []
    for row in sess.query(FHP).all():
        if row.key == str(key) and row.octave == int(octave):
            item_list.append(round(row.fh_1, 2))
            item_list.append(round(row.fh_2, 2))
            item_list.append(round(row.fh_3, 2))
            item_list.append(round(row.fh_4, 2))
            item_list.append(round(row.fh_5, 2))
            item_list.append(round(row.fh_6, 2))
            if row.fh_7:
                item_list.append(round(row.fh_7, 2))
    return item_list


def update_fhp_values(key, octave, bore):
    id_num = 0
    item_list = []
    items = {1: 'id', 2: 'key', 3: 'octave', 4: 'scale', 5: 'fh_1', 6: 'fh_2', 7: 'fh_3', 8: 'fh_4', 9: 'fh_5',
             10: 'fh_6', 11: 'fh_7'}
    while True:
        print()
        for row in sess.query(FHP).all():
            if row.key == key and row.octave == int(octave):
                print(f'(1) {(bore * row.fh_1):.2f} (2) {(bore * row.fh_2):.2f} (3) {(bore * row.fh_3):.2f} '
                      f'(4) {(bore * row.fh_4):.2f} (5) {(bore * row.fh_5):.2f} (6) {(bore * row.fh_6):.2f} '
                      f'(7) {(bore * row.fh_7):.2f}')
                id_num = row.id
                item_list.append(row.fh_1)
                item_list.append(row.fh_2)
                item_list.append(row.fh_3)
                item_list.append(row.fh_4)
                item_list.append(row.fh_5)
                item_list.append(row.fh_6)
                item_list.append(row.fh_7)

        item = input('\nSelect item number to modify: ')
        if not item:
            break
        spacing(10)
        if item:
            fh_value = input('Enter updated value (inches): ')
            if not fh_value:
                break
            spacing(2)
            if fh_value:
                updated_item = round(float(fh_value)/bore, 2)
                spacing(10)
                u = update(FHP)
                u = u.values({items[int(item) + 4]: updated_item})
                u = u.where(FHP.id == id_num)
                sess.execute(u)
                sess.commit()


def add_fhp_values():
    entries = []
    entry_list = ('key', 'octave', 'scale', 'fh_1', 'fh_2', 'fh_3', 'fh_4', 'fh_5', 'fh_6', 'fh_7')

    for name in entry_list:
        entries.append(input(f'Enter {name}: '))

    sess.add(FHP(key=entries[0], octave=entries[1], scale=entries[2], fh_1=entries[3], fh_2=entries[4], fh_3=entries[5]
                 , fh_4=entries[6], fh_5=entries[7], fh_6=entries[8], fh_7=entries[9]))

    sess.commit()
