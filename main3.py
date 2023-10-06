import scales
import datetime
from math import sqrt
import update_fhp
from my_flute_class import MyFlute
import take_order
import save_percents


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


def get_temp_offset(ambient_temp_f: float) -> float:
    """
    :param ambient_temp_f: the ambient temperature in degrees F
    :return: the number of hertz to change the tuning frequency by
    """
    offset_calc = (12600.535*sqrt((ambient_temp_f+459.4)/459.4))/30.80006182 - 440

    return offset_calc


def spacing(nums):
    for lines in range(nums):
        print()


def blank_size(flute):
    spacing(20)
    flute.print_sizing()
    input(':')
    spacing(10)


def fh_placement(flute):
    spacing(20)
    print(f'Flute Key: {flute.get_flute_key()}({flute.get_flute_octave()})')
    flute.get_finger_hole_placements()
    print(f'----------------------------')
    flute.print_fh_placement()
    print(f'----------------------------')
    # input('...')
    spacing(10)


def get_ref_offset(flute):
    spacing(20)
    tuner_ref = flute.get_tuner_ref()
    print(f'----------------------------')
    print(f'Tuner reference = {tuner_ref:.1f} Hz')
    print(f'----------------------------')
    input(':')
    spacing(10)


def get_scale_notes(flute):
    spacing(20)
    scales.main(flute.get_flute_key())
    input(':')
    spacing(20)


def craft_flute():
    spacing(10)
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
        print(f'6. Export FHP table        *')
        print(f'****************************')

        selection = select_script()

        if selection == 1:
            blank_size(flute)

        if selection == 2:
            get_ref_offset(flute)

        if selection == 3:
            get_scale_notes(flute)

        if selection == 4:
            spacing(20)
            flute = MyFlute.flute_key()
            print(flute.get_flute_key())
            spacing(10)

        if selection == 5:
            fh_placement(flute)

        if selection == 6:
            save_percents.main()
            spacing(10)

        if not selection:
            break


def main():

    while True:
        spacing(10)
        print(f'****************************')
        print(f'1. Craft Flute             *')
        print(f'2. Take Orders             *')
        print(f'3. View Orders             *')
        print(f'4. View Sales              *')
        print(f'****************************')

        selection = select_script()
        spacing(2)

        if selection == 1:
            craft_flute()

        if selection == 2:
            take_order.main()

        if selection == 3:
            take_order.view_orders()

        if selection == 4:
            take_order.view_sales()

        if not selection:
            exit()


if __name__ == '__main__':
    main()