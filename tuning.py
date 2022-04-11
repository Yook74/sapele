
def get_tuning_freq() -> float:
    """gets the turning frequency from the user and returns it as a float"""


def get_ambient_temp_f() -> float:
    """gets the current ambient temperature in degrees F and returns it as a float"""


def get_temp_offset(ambient_temp_f: float) -> float:
    """
    :param ambient_temp_f: the ambient temperature in degrees F
    :return: the number of hertz to change the tuning frequency by
    """


while True:
    ambient_temp = get_ambient_temp_f()
    freq_offset = get_temp_offset(ambient_temp)
    print(f'The frequency offset is {freq_offset} Hz')

    tuning_freq = get_tuning_freq() + freq_offset
    print(f'Tune to {tuning_freq} Hz')
