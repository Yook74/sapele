"""Import functions to and select which one to run"""

import tuning
import blank_sizing
import measurement_data_entry
import fh_data_entry


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


def main():

    while True:

        print(f'****************************')
        print(f'1. Get Blank Sizing        *')
        print(f'2. Get Tuner Ref Offset    *')
        print(f'3. Data Entry (Pre-Tune)   *')
        print(f'4. FH Data (Post-Tune)     *')
        print(f'****************************')

        num_select = select_script()

        if num_select == 1:
            blank_sizing.main()
        if num_select == 2:
            tuning.main()
        if num_select == 3:
            measurement_data_entry.main()
        if num_select == 4:
            fh_data_entry.main()


if __name__ == '__main__':
    main()
