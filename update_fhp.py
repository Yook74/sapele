from database.models import FHP
from database.connection import get_session
from sqlalchemy import update

sess = get_session()


def spacing(nums):
    for lines in range(nums):
        print()


def get_fhp_values(key, octave):
    item_list = []
    spacing(10)
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
    item_list = []
    items = {1: 'id', 2: 'key', 3: 'octave', 4: 'fh_1', 5: 'fh_2', 6: 'fh_3', 7: 'fh_4', 8: 'fh_5', 9: 'fh_6'
             , 10: 'fh_7'}
    while True:
        for row in sess.query(FHP).all():
            if row.key == key and row.octave == int(octave):
                print(f'(ID {row.id}), (Key) {row.key}, (Octave) {row.octave}, (Bore Length) {row.bore_length}, (FH1)'
                      f' {(bore * row.fh_1):.2f}, (FH2) {(bore * row.fh_2):.2f}, (FH3) {(bore * row.fh_3):.2f}, '
                      f'(FH4) {(bore * row.fh_4):.2f}, (FH5) {(bore * row.fh_5):.2f}, (FH6) {(bore * row.fh_6):.2f}, '
                      f'(FH7) {(bore * row.fh_7):.2f}')

        id_num = (input('\nSelect ID number: '))
        if not id_num:
            break
        spacing(10)

        for row in sess.query(FHP).all():
            print(f'(1) {(bore * row.fh_1):.2f} (2) {(bore * row.fh_2):.2f} (3) {(bore * row.fh_3):.2f} '
                  f'(4) {(bore * row.fh_4):.2f} (5) {(bore * row.fh_5):.2f} (6) {(bore * row.fh_6):.2f} '
                  f'(7) {(bore * row.fh_7):.2f}')
            if row.id == id_num:
                item_list.append(row.fh_1)
                item_list.append(row.fh_2)
                item_list.append(row.fh_3)
                item_list.append(row.fh_4)
                item_list.append(row.fh_5)
                item_list.append(row.fh_6)
                item_list.append(row.fh_7)

        item = input('\nSelect item number to modify: ')
        if item:
            fh_value = input('Enter updated value (inches): ')
            if fh_value:
                updated_item = round(float(fh_value)/bore, 3)
                spacing(10)

                u = update(FHP)
                u = u.values({items[int(item) + 3]: updated_item})
                u = u.where(FHP.id == id_num)
                sess.execute(u)
                sess.commit()

