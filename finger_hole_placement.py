"""Returns finger hole Placement Recommendations"""
from database.models import Note, Scale
from database.connection import get_session

sess = get_session()


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


def get_key():
    """Select key of the scale"""
    while True:
        value = input('Enter a key (for example, C#): ')
        try:
            return value
        except ValueError:
            print('Invalid key name')


def get_octave():
    """Select octave"""
    while True:
        value = input(f'Enter the Octave (3, 4, or 5): ')
        try:
            return int(value)
        except ValueError:
            print('Invalid Input')


def get_scale():
    """Allows the user to choose a scale from the database and returns which scale they chose"""
    for scale in sess.query(Scale).all():
        print(f'{scale.id}: {scale.name}')

    while True:
        scale_id = input('Please enter the number of a scale: ')
        try:
            scale_id = int(scale_id)
        except ValueError:
            print('Invalid input')
        return scale_id


def get_all_finger_hole_placements(bore_length: float):
    """Get finger hole placements based on bore length percentage"""

    finger_hole_percents = [.68, .62, .56, .48, .40, .33]
    finger_holes_absolute = []
    for percent in finger_hole_percents:
        finger_holes_absolute.append(percent * bore_length)

    return finger_holes_absolute


def main():

    try:

        calc_factor = get_calc_factor(default=.315)
        bore_length = get_bore_length()
        max_distance, min_distance = get_top_bottom_hole_placements(bore_length, calc_factor)
        print(f'----------------------------')
        print(f'CALC FACTOR: {calc_factor:.3f} inches\nMAX: {max_distance:.2f} inches\nMIN: {min_distance:.2f} inches')

        key = get_key()
        octave = get_octave()
        scale = get_scale()
        # TODO I want to pull percentages based on key and octave and scale from the database

        finger_holes = get_all_finger_hole_placements(bore_length)
        print(f'----------------------------')
        print(f'Key: {key}, Octave: {octave:d}, Scale: {scale:d}')

        for index, holes in enumerate(finger_holes):
            print(f'FH_{index+1}: {holes:.2f}')

        print(f'----------------------------\n')

    finally:
        sess.close()


if __name__ == '__main__':
    main()
