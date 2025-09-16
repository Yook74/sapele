import scales
import datetime
from my_flute_class import MyFlute
import take_order
import save_tables
import os
import time


def select_script() -> int:
    """Selects script to run"""
    while True:
        value = input(f'SELECT NUMBER: ')
        if not value:
            break

        try:
            return int(value)
        except ValueError:
            print('Invalid Input')


def spacing(nums):
    for lines in range(nums):
        print()


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
    os.system('cls' if os.name == 'nt' else 'clear')
    scales.main(flute.get_flute_key())
    input(':')


def craft_flute():
    os.system('cls' if os.name == 'nt' else 'clear')
    flute = MyFlute.flute_key()
    spacing(2)

    while True:
        print(f'< Key {flute.get_flute_key()} >')
        print(f'****************************')
        print(f'1. Get Blank Sizing        *')
        print(f'2. Get Tuner Ref Offset    *')
        print(f'3. Get Scale Notes         *')
        print(f'4. Change Key              *')
        print(f'5. FH Placement            *')
        print(f'6. Export Tables to CSV    *')
        print(f'****************************')

        selection = select_script()

        if selection == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            blank_size(flute)

        elif selection == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            get_ref_offset(flute)

        elif selection == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            get_scale_notes(flute)

        elif selection == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            flute = MyFlute.flute_key()
            print(flute.get_flute_key())

        elif selection == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            fh_placement(flute)

        elif selection == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            save_tables.main()

        elif not selection:
            break

        os.system('cls' if os.name == 'nt' else 'clear')


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:

        print(f'****************************')
        print(f'1. Craft Flute             *')
        print(f'2. Take Orders             *')
        print(f'3. View Orders             *')
        print(f'4. View Sales              *')
        print(f'test')
        print(f'****************************')

        selection = select_script()
        spacing(2)

        if selection == 1:
            craft_flute()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif selection == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            take_order.main()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif selection == 3:
            take_order.view_orders()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif selection == 4:
            take_order.view_sales()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif not selection:
            exit()


if __name__ == '__main__':
    main()
    os.system('cls' if os.name == 'nt' else 'clear')