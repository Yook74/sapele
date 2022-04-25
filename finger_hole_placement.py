"""Returns finger hole Placement Recommendations"""
from database.models import Note, Scale
from database.connection import get_session
from typing import Type, Callable, Optional


sess = get_session()

def get_value_from_user(prompt: str, type_: Type = str, default=None, validation_func: Optional[Callable] = None):
    """ a generic function to get an inputted value from the user over the command line

    :param prompt: a string like "enter your age" which the user should respond to
    :param type_: this function will attempt to convert the response to the given type before returning it
    :param default: this will be returned if the user enters nothing.
        It will also be appended to the prompt for the user's convenience
    :param validation_func: a one-parameter function that returns True if the value is valid and False otherwise
    :return: the value entered by the user converted to the given type or the default value
    """

    if default:
        prompt += f' (default: {default}): '
    else:
        prompt += ': '

    while True:
        value = input(prompt)

        if not value:
            return default

        try:
            value = type_(value)
        except ValueError:
            print('invalid input')
            continue

        if validation_func:
            if validation_func(value):
                return value
            else:
                print('invalid input')
        else:
            return value


def validate_octave(octave):
    return 3 <= octave <= 5


def get_scale():
    """Allows the user to choose a scale from the database and returns which scale they chose"""
    for scale in sess.query(Scale).all():
        print(f'{scale.id}: {scale.name}')

    while True:
        scale_id = input('Select the Scale: ')
        try:
            scale_id = int(scale_id)
        except ValueError:
            print('Invalid input')
        return scale_id


def get_top_bottom_hole_placements(bore_length: float, calc_factor: float):
    """Get Top and Bottom hole placements"""
    return bore_length - (bore_length * calc_factor), bore_length * calc_factor


def get_all_finger_hole_placements(bore_length: float):
    """Get finger hole placements based on bore length percentage"""

    # TODO These percent value would be derived from the average of the stored database values
    finger_hole_percents = [.68, .62, .56, .48, .40, .33]
    finger_holes_absolute = []
    for percent in finger_hole_percents:
        finger_holes_absolute.append(percent * bore_length)

    return finger_holes_absolute


def main():

    try:

        print('\n----------------------------')
        calc_factor = get_value_from_user('Enter Calculation factor', type_=float, default=.315)
        bore_length = get_value_from_user('Enter the Bore Length', type_=float)
        max_distance, min_distance = get_top_bottom_hole_placements(bore_length, calc_factor)
        print('----------------------------')
        print(f'CALC FACTOR: {calc_factor:.3f} inches\nMAX: {max_distance:.2f} inches\nMIN: {min_distance:.2f} inches')
        print('----------------------------\n')
        print('PERCENTAGE BASED:')
        key = get_value_from_user('Enter the Key (i.e. C#)', type_=str)
        octave = get_value_from_user('Enter the Octave (3, 4, or 5)', type_=int, default=4,
                                     validation_func=validate_octave)
        print('----------------------------')
        scale = get_scale()

        # TODO Using Key, Octave, and Scale, I want to pull percentages based the average of the data stored
        #  in the database from the finger_hole_measurement_entry.py script
        finger_holes = get_all_finger_hole_placements(bore_length)
        print(f'----------------------------')
        print(f'KEY: {key}, OCTAVE: {octave:d}, SCALE: {scale:d}')

        for index, holes in enumerate(finger_holes):
            print(f'FH_{index+1}: {holes:.2f}')

        print(f'----------------------------\n')

    finally:
        sess.close()


if __name__ == '__main__':
    main()
