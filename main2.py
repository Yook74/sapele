import scales
from my_flute_class import MyFlute
import fltue_orders as order
import os


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
    scales.main(flute.get_flute_key())
    input(':')


def my_orders():
    while True:
        print('****************************')
        print('1. Take Order              *')
        print('2. View Orders             *')
        print('3. Update Order            *')
        print('4. View Customer Orders    *')
        print('****************************')

        selection = input(f'SELECT NUMBER: ')

        if selection == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            order.take_order()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif selection == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            order.view_orders()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif selection == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            order.update_order()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif selection == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            order.view_customer_orders()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif not selection:
            break


def craft_flute():
    flute = MyFlute.flute_key()
    spacing(2)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'< Key {flute.get_flute_key()} >')
        print(f'****************************')
        print(f'1. Get Blank Sizing        *')
        print(f'2. Get Tuner Ref Offset    *')
        print(f'3. Get Scale Notes         *')
        print(f'4. Change Key              *')
        print(f'5. FH Placement            *')
        print(f'****************************')

        selection = select_script()

        if selection == 1:
            blank_size(flute)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif selection == 2:
            get_ref_offset(flute)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif selection == 3:
            get_scale_notes(flute)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif selection == 4:
            flute = MyFlute.flute_key()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(flute.get_flute_key())

        elif selection == 5:
            fh_placement(flute)
            os.system('cls' if os.name == 'nt' else 'clear')


        elif not selection:
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'****************************')
        print(f'1. Craft                   *')
        print(f'2. Orders                  *')
        print(f'****************************')

        selection = select_script()
        spacing(2)

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