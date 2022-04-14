"""Import functions to and select which one to run"""

import tuning
import blank_sizing
import finger_hole_placement


def select_script() -> int:
    """Selects script to run"""
    while True:
        value = input(f'SELECT NUMBER: Blank Sizing = 1 , Hole Placement = 2 , Tuning Offset = 3 , Scale = 4\n')

        try:
            return int(value)
        except ValueError:
            print ('Invalid Input')


def main():
    while True:
        1
        num_select = select_script()

        if num_select == 1:
            blank_sizing.main()
        if num_select == 2:
            finger_hole_placement.main()
        if num_select == 3:
            tuning.main()


if __name__ == '__main__':
    main()

