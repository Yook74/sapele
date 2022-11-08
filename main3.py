import scales
from math import sqrt
from my_flute_class import MyFlute


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


def main():
    flute = MyFlute.flute_key()
    flute.print_sizing()
    input(':::')
    spacing(10)

    while True:
        print(f'****************************')
        print(f'1. Get Blank Sizing        *')
        print(f'2. Get FH Placement        *')
        print(f'3. Get Tuner Ref Offset    *')
        print(f'4. Get Scale Notes         *')
        print(f'****************************')

        spacing(3)

        num_select = select_script()

        if num_select == 1:
            spacing(20)
            flute.print_sizing()
            input('...')
            spacing(10)
        if num_select == 2:
            spacing(20)
            print(f'Flute Key: {flute.get_flute_key()}({flute.get_flute_octave()})')
            flute.get_finger_hole_placements()
            flute.print_fh_placement()
            input('...')
            spacing(10)
        if num_select == 3:
            spacing(20)
            tuner_ref = flute.get_tuner_ref()
            print(f'----------------------------')
            print(f'Tuner reference = {tuner_ref:.1f} Hz')
            print(f'----------------------------\n')
            input('...')
            spacing(10)
        if num_select == 4:
            spacing(20)
            scales.main()
            input('...')
            spacing(20)


if __name__ == '__main__':
    main()

