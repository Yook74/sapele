from database.models import Note, Scale
from database.connection import get_session
from typing import Type, Callable, Optional
import csv
from os import path
from statistics import mean as average

sess = get_session()


"""This script is used to gather flute measurement data, prior top placing the finger holes"""


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


def get_top_bottom_hole_placements(bore_length: float, calc_factor: float):
    """Get Top and Bottom hole placements"""
    return bore_length - (bore_length * calc_factor), bore_length * calc_factor


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


def get_all_finger_hole_placements(bore_length: float):
    """Get finger hole placements based on bore length percentage"""

    # TODO These percent value would be derived from the average of the stored database values
    finger_hole_percents = [.68, .62, .56, .48, .40, .33]
    finger_holes_absolute = []
    for percent in finger_hole_percents:
        finger_holes_absolute.append(percent * bore_length)

    return finger_holes_absolute


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


def validate_octave(octave):
    return 3 <= octave <= 5


def enter_seed_values(prompt: str):
    """Enter Finger Hole seed values as comma separated string if new file encountered"""
    while True:
        value = input(prompt)
        if not value:
            exit()

        try:
            return str(value)
        except ValueError:
            print('Invalid Input')


def main():
    # TODO I want to be able to store this data and be able to retrieve it as averaged data
    #  based on key, octave, and scale. I would also like to retrieve individual records
    #  (searched by key, octave, and/or customer)

    print(f'\n----------------------------')
    customer_name = get_value_from_user('Enter the Customer Name: ', default='Shop Stock')
    key = get_value_from_user('Enter the Key', type_=str)
    octave = get_value_from_user('Enter the Octave', type_=int, default=4, validation_func=validate_octave)
    scale_num = get_scale()
    scale = sess.query(Scale).filter_by(id=scale_num).first()
    total_length = get_value_from_user('Enter the Total Length', type_=float)
    bore_length = get_value_from_user('Enter the Bore Length', type_=float)
    bore_diameter = get_value_from_user('Enter the Bore Diameter', type_=float)
    tsh_width = get_value_from_user('Enter the TSH Width', type_=float)
    tsh_length = get_value_from_user('Enter the TSH Length',  type_=float)
    flue_depth = get_value_from_user('Enter the Flue Depth', type_=float, default=.085)
    wall_thickness = get_value_from_user('Enter the Wall Thickness',  type_=float, default=.1875)

    file_path = f'records/FH_Percents.csv'
    if not path.exists(file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Key_Octave_Scale', 'FH1', 'FH2', 'FH3', 'FH4', 'FH5', 'FH6'])

    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        percent_values = enter_seed_values('Enter Initial Percentage Values as comma separated string: ')
        writer.writerow(percent_values.split(','))

    with open(file_path) as file:
        fh_file = csv.DictReader(file)

        avg_values = []



    finger_holes = get_all_finger_hole_placements(bore_length)
    print(f'----------------------------')

    print(f'\n---------------------------')
    print('RECOMMENDED PLACEMENT:')
    for index, holes in enumerate(finger_holes):
        print(f'FH_{index+1}: {holes:.2f}')
    print(f'---------------------------\n')

    sess.close()


if __name__ == '__main__':
    main()
