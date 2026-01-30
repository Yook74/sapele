from my_flute_class import MyFlute
import fltue_orders as order
import select_script as ss
import pandas as pd
import os


def blank_size(flute):
    flute.print_sizing()
    input(':')


def fh_placement(flute):
    print(f'Flute Key: {flute.get_flute_key()}({flute.get_flute_octave()})')
    flute.get_finger_hole_placements()
    print(f'----------------------------')


def get_ref_offset(flute):
    tuner_ref = flute.get_tuner_ref()
    print(f'----------------------------')
    print(f'Tuner reference = {tuner_ref:.1f} Hz')
    print(f'----------------------------')
    input(':')


def get_scale_notes(flute):
    fp_1 = r'C:\Users\carl.young\Documents\sapele\csv_stuff\notes_table.csv'
    fp_2 = r'C:\Users\carl.young\Documents\sapele\csv_stuff\intervals.csv'
    key = flute.get_flute_key()
    df1 = pd.read_csv(fp_1)
    row = df1[df1['0'].str.contains(f'({key})', regex=False)]\
        .to_string(index=False, justify='center', header=None).split()
    df2 = pd.read_csv(fp_2)
    scales = df2['0'].tolist()
    size = len(scales)
    print()
    for num in range(0, size, 1):
        print(f'{num +1}: {scales[num]}')
    sel = int(input('\nSelect scale: '))-1
    if not sel:
        sel = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    row2 = df2[df2['0'].str.contains(scales[sel], regex=False)]\
        .to_string(index=False, justify='center', header=None).split()
    print(f'\n< Scale: {key} - {scales[sel]} >\n')
    for num in range(7, 0, -1):
        if row2[num] != "NaN":
            print('FH:', [num], ': ', row[int(float(row2[num]))])
    print()
    input(':')


def my_orders():
    while True:
        print()
        print('****************************')
        print('1. Take Order              *')
        print('2. View Orders             *')
        print('3. Update Order            *')
        print('4. View Customer Orders    *')
        print('****************************')

        selection = ss.select_script()

        if selection == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            order.take_order()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif selection == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            order.view_orders()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif selection == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            order.update_order()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif selection == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            order.view_customer_orders()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif not selection:
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        os.system('cls' if os.name == 'nt' else 'clear')


def craft_flute():
    flute = MyFlute.flute_key()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print(f'< Key {flute.get_flute_key()} >')
        print(f'****************************')
        print(f'1. Get Blank Sizing        *')
        print(f'2. Get Tuner Ref Offset    *')
        print(f'3. Get Scale Notes         *')
        print(f'4. Change Key              *')
        print(f'5. FH Placement            *')
        print(f'****************************')

        selection = ss.select_script()

        if selection == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            blank_size(flute)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif selection == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            get_ref_offset(flute)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif selection == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            get_scale_notes(flute)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif selection == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            flute = MyFlute.flute_key()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(flute.get_flute_key())

        elif selection == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            fh_placement(flute)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif not selection:
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        print()
        print('****************************')
        print('1. Craft                   *')
        print('2. Orders                  *')
        print('****************************')

        selection = ss.select_script()
        print()

        if selection == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            craft_flute()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif selection == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            my_orders()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif not selection:
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()


if __name__ == '__main__':
    main()
    os.system('cls' if os.name == 'nt' else 'clear')