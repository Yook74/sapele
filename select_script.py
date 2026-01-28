import os


def select_script() -> int:
    """Selects script to run"""
    while True:
        value = input(f'SELECT NUMBER: ')
        if not value:
            break

        try:
            return int(value)
        except ValueError:
            print('Invalid Input')
