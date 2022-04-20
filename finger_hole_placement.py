"""Returns Top and Bottom hole Placement Recommendations"""

def get_bore_length() -> float:
    """Get Bore Length"""
    while True:
        value = input(f'Enter the bore length: ')
        try:
            return float(value)
        except ValueError:
            print('Invalid Input')


def get_calc_factor(default=None) -> float:
    """ Assigns the bore factor used in bore length calculation"""
    while True:
        value = input(f'Enter the calculation factor (.315 is default): ')

        if not value:
            return default

        try:
            return float(value)
        except ValueError:
            print('Invalid Input')


def get_top_bottom_hole_placements(bore_length: float, calc_factor: float):
    """Get Top and Bottom hole placements"""
    return bore_length - (bore_length * calc_factor), bore_length * calc_factor


def get_all_finger_hole_placements(bore_length: float):
    """Get finger hole placements based on bore length percentage"""
    finger_hole_percents = [.68, .61, .54, .46, .38, .30]
    finger_holes_absolute = []
    for percent in finger_hole_percents:
        finger_holes_absolute.append(percent * bore_length)

    return finger_holes_absolute


def main():

    calc_factor = get_calc_factor(default=.315)
    bore_length = get_bore_length()
    max_distance, min_distance = get_top_bottom_hole_placements(bore_length, calc_factor)
    print(f'----------------------------')
    print(f'CALC FACTOR: {calc_factor:.3f} inches\nMAX: {max_distance:.2f} inches\nMIN: {min_distance:.2f} inches')

    finger_holes = get_all_finger_hole_placements(bore_length)

    for index, holes in enumerate(finger_holes):
        print(f'FH_{index+1}: {holes:.2f}')

    print(f'----------------------------\n')


if __name__ == '__main__':
    main()
