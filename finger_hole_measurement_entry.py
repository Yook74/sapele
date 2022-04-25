"""allows user to enter finger hole placement measurements per key and octave to the database.
measurements will be used to retrieve averaged hole placements data to the user"""
from typing import Type, Callable, Optional


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


def main():


if __name__ == '__main__':
    main()