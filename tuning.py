from math import sqrt


def get_reference_freq() -> float:
    """gets the reference frequency from the user and returns it as a float"""
    while True:
        freq_ref = input('Enter the reference frequency in Hz (default is 440): ')

        if freq_ref:
            freq_ref = float(freq_ref)
        else:
            freq_ref = 440

        if freq_ref < 100 or freq_ref > 1000:
            print('Enter a number greater than 100')
        else:
            return freq_ref


def get_ambient_temp_f() -> float:
    """gets the current ambient temperature in degrees F and returns it as a float"""
    while True:
        tuning_temp = input('Enter the ambient temperature in Deg (F): ')
        try:
            return float(tuning_temp)
        except ValueError:
            print('Invalid input')


def get_temp_offset(ambient_temp_f: float) -> float:
    """
    :param ambient_temp_f: the ambient temperature in degrees F
    :return: the number of hertz to change the tuning frequency by
    """
    offset_calc = (12600.535*sqrt((ambient_temp_f+459.4)/459.4))/30.80006182 - 440

    return offset_calc


def main():

    ambient_temp = get_ambient_temp_f()
    freq_offset = get_temp_offset(ambient_temp)
    freq_ref = get_reference_freq()
    tuning_freq = freq_ref + freq_offset

    print(f'----------------------------')
    print(f'Tuner reference = {tuning_freq:.1f} Hz')
    print(f'----------------------------\n')


if __name__ == '__main__':
    main()
