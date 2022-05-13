"""This script is used to record finger hole placements after tuning"""
from database.models import Note, Scale
from database.connection import get_session
from typing import Type, Callable, Optional
import csv
from os import path

sess = get_session()


def get_value_from_user(prompt: str, type_: Type = str, validation_func: Optional[Callable] = None):
    """ a generic function to get an inputted value from the user over the command line

    :param prompt: a string like "enter your age" which the user should respond to
    :param type_: this function will attempt to convert the response to the given type before returning it
    :param default: this will be returned if the user enters nothing.
        It will also be appended to the prompt for the user's convenience
    :param validation_func: a one-parameter function that returns True if the value is valid and False otherwise
    :return: the value entered by the user converted to the given type or the default value
    """

    while True:
        value = input(prompt)

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


def validate_hole_num_range(fh_num):
    return 1 <= fh_num <= 7


def get_scale_names():
    scale_names = ['Minor Pent', 'Major', 'Mojave', 'Mayan', 'Magen Avot']
    while True:

        print(f'****************************')
        for index, name in enumerate(scale_names):
            print(f'{index + 1} : {name}')
        print(f'****************************')

        num_select = select_script()

        return scale_names.pop(num_select-1)



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


def enter_

def select_finger_hole(type_: Type = str, validation_func: Optional[Callable] = None):
    """Selects script to run"""

    while True:
        value = input(f'SELECT FH: ')
        if not value:
            exit()

        try:
            return type_(value)
        except ValueError:
            print('Invalid Input')

        if validation_func:
            if validation_func(value):
                return value
            else:
                print('invalid input')
        else:
            return value


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
    """ Main """

    key = get_value_from_user('Enter the Key: ', type_=str)
    octave = get_value_from_user('Enter the Octave: ', type_=int, validation_func=validate_octave)
    scale = get_scale_names()

    print (f'Key: {key} Octave: {octave} Scale: {scale}\n')
    print(f'{key}_{octave}_{scale}\n')

    file_path = f'records/{key}_{octave}_{scale}.csv'

    if not path.exists(file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['FH1', 'FH2', 'FH3', 'FH4', 'FH5', 'FH6'])
            enter_seed_values('Enter Initial Percentage Values as comma separated string: ')

    while True:

        num_select = select_finger_hole()

        if int(num_select) == 1:
            print('this worked')



sess.close()


if __name__ == '__main__':
    main()