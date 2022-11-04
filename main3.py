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


def main():
    flute = MyFlute.flute_key()
    print(flute.print_sizing())

    while True:

        print(f'****************************')
        print(f'1. Get Blank Sizing        *')
        print(f'2. Get Tuner Ref Offset    *')
        print(f'3. Data Entry (Pre-Tune)   *')
        print(f'4. FH Entry (Post-Tune)    *')
        print(f'****************************')

        num_select = select_script()

        if num_select == 1:
            flute.print_sizing()
        if num_select == 2:
            print()
        if num_select == 3:
            print()
        if num_select == 4:
            flute.get_finger_hole_placements()
            flute.print_fh_placement()


if __name__ == '__main__':
    main()
