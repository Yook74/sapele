from math import sqrt
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



def get_temp_offset(ambient_temp_f: float) -> float:
    """
    :param ambient_temp_f: the ambient temperature in degrees F
    :return: the number of hertz to change the tuning frequency by
    """
    offset_calc = (12600.535*sqrt((ambient_temp_f+459.4)/459.4))/30.80006182 - 440

    return offset_calc


def main():


    ambient_temp = get_value_from_user('Enter the ambient temperature in Deg: ', type_=int, default=72)
    freq_ref = get_value_from_user('Enter Reference Frequency in Hz: ', type_=int, default=440)
    freq_offset = get_temp_offset(ambient_temp)
    tuning_freq = freq_ref + freq_offset


    print(f'----------------------------')
    print(f'Tuner reference = {tuning_freq:.1f} Hz')
    print(f'----------------------------\n')


if __name__ == '__main__':
    main()
