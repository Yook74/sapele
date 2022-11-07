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


def main():
    flute = MyFlute.flute_key()
    print(flute.print_sizing())

    #  ambient_temp = 72
    #  tuner_ref = 440
    while True:

        print(f'****************************')
        print(f'1. Get Blank Sizing        *')
        print(f'2. Get FH Placement        *')
        print(f'3. Get Tuner Ref Offset    *')
        print(f'4. ??                      *')
        print(f'****************************')

        num_select = select_script()

        if num_select == 1:
            flute.print_sizing()
        if num_select == 2:
            print(f'Flute Key: {flute.get_flute_key()}({flute.get_flute_octave()})')
            flute.get_finger_hole_placements()
            flute.print_fh_placement()
        if num_select == 3:
            tuner_ref = flute.get_tuner_ref()
            print(f'----------------------------')
            print(f'Tuner reference = {tuner_ref:.1f} Hz')
            print(f'----------------------------\n')
        if num_select == 4:
            print()


if __name__ == '__main__':
    main()
