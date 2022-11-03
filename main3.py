from my_flute_class import MyFlute


if __name__ == '__main__':

    print(f'----------------------------')
    flute = MyFlute.get_blank_sizing()

    flute.print_sizing()

    flute.get_finger_hole_placements()

    flute.print_fh_placement()

