from database.models import Note, Scale, Customer
from database.connection import get_session
import os

sess = get_session()


def use_key(my_key):
    """ """
    try:
        return Note.from_name(sess, my_key)
    except ValueError:
        print('Invalid key name')


def get_scale() -> Scale:
    """Allows the user to choose a scale from the database and returns which scale they chose"""
    print(f'----------------------------')
    for scale in sess.query(Scale).all():
        print(f'{scale.id}: {scale.name}')
    print(f'----------------------------')

    while True:
        scale_id = input('Select scale: ')
        try:
            scale_id = int(scale_id)
        except ValueError:
            print('Invalid input')
            continue

        scale = sess.query(Scale).filter_by(id=scale_id).first()

        if scale is None:
            print('Invalid scale number')
        else:
            return scale


def spacing(nums):
    for lines in range(nums):
        print()


def main(my_key):
    try:
        key = use_key(my_key)
        selected_key = f'Key = {my_key}'
        os.system('cls' if os.name == 'nt' else 'clear')
        scale = get_scale()
        num_holes = len(scale.offsets)
        # spacing(20)
        print(selected_key)
        print(f'----------------------------')
        for note in range(num_holes):
            fh_hole = ((num_holes-1) - int(note))
            print(f' FH {fh_hole + 1} - {scale.get_notes(key)[fh_hole].name}')
        print(f'----------------------------')

    finally:
        sess.close()


if __name__ == '__main__':
    main()
