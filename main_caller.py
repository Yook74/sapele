"""Import functions to and select which one to run"""

import tuning
import blank_sizing
import finger_hole_placement
import scales


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
        print(f'1. Get Blank Size          *')
        print(f'2. Get Finger Holes        *')
        print(f'3. Get Tuning Offset       *')
        print(f'4. Get Scale Notes         *')
        print(f'****************************')

        num_select = select_script()

        if num_select == 1:
            blank_sizing.main()
        if num_select == 2:
            finger_hole_placement.main()
        if num_select == 3:
            tuning.main()
        if num_select == 4:
            scales.main()


if __name__ == '__main__':
    main()
