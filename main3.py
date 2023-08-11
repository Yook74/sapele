import scales
import datetime
from math import sqrt
from my_flute_class import MyFlute
import take_order
# from database.models import Customer


def select_script() -> int:
    """Selects script to run"""
    while True:
        value = input(f'SELECT NUMBER: ')
        if not value:
            exit()

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
    input('...')
    spacing(10)


def fh_placement(flute):
    spacing(20)
    print(f'Flute Key: {flute.get_flute_key()}({flute.get_flute_octave()})')
    flute.get_finger_hole_placements()
    print(f'----------------------------')
    flute.print_fh_placement()
    print(f'----------------------------')
    input('...')
    spacing(10)


def get_ref_offset(flute):
    spacing(20)
    tuner_ref = flute.get_tuner_ref()
    print(f'----------------------------')
    print(f'Tuner reference = {tuner_ref:.1f} Hz')
    print(f'----------------------------\n')
    input('...')
    spacing(10)


def get_scale_notes(flute):
    spacing(20)
    scales.main(flute.get_flute_key())
    input('...')
    spacing(20)


# def orders():
#     spacing(10)
#
#     while True:
#         print(f'****************************')
#         print(f'1. Take Order              *')
#         print(f'2. Update Order            *')
#         print(f'3. Update customer         *')
#         print(f'****************************')
#
#         spacing(2)
#
#         num_select = select_script()
#
#         if num_select == 1:
#             customer_id = take_order.customer_entry()
#             take_order.take_order(customer_id)
#             print(customer_id)
#
#         if num_select == 2:
#             print(2)
#
#         if num_select == 3:
#             print(3)


def main():

    flute = MyFlute.flute_key()


    spacing(10)

    while True:
        print(f'< Key {flute.get_flute_key()} >')
        print(f'****************************')
        print(f'1. Get Blank Sizing        *')
        print(f'2. Get FH Placement        *')
        print(f'3. Get Tuner Ref Offset    *')
        print(f'4. Get Scale Notes         *')
        print(f'5. Change Key              *')
        print(f'6. Orders                  *')
        print(f'****************************')

        spacing(2)

        num_select = select_script()

        if num_select == 1:
            blank_size(flute)

        if num_select == 2:
            fh_placement(flute)

        if num_select == 3:
            get_ref_offset(flute)

        if num_select == 4:
            get_scale_notes(flute)

        if num_select == 5:
            spacing(20)
            flute = MyFlute.flute_key()
            print(flute.get_flute_key())
            spacing(10)

        if num_select == 6:
            take_order.main()



if __name__ == '__main__':
    main()