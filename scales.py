from database.models import Note, Scale, Customer
from database.connection import get_session

sess = get_session()


def get_key() -> Note:
    """Allows the user to enter a note which will be the key of the scale"""

    while True:
        name = input('Enter the flute key: ').upper()
        if not len(name) == 1:
            name = name[0] + (name[1].lower())

        try:
            return Note.from_name(sess, name)
        except ValueError:
            print('Invalid key name')


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
        scale_id = input('Please enter the number of a scale: ')
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
        print(f'Using Key of {my_key}')
        change_key = input('Change Key?: ').upper()
        if not change_key:
            key = use_key(my_key)
            selected_key = f'Key = {my_key}'
        else:
            key = use_key(change_key)
            selected_key = f'Key = {change_key}'

        spacing(20)
        scale = get_scale()
        spacing(20)
        print(selected_key)
        print(f'----------------------------')
        for note in range(6):
            fh_hole = (5 - int(note))
            print(f' FH {fh_hole + 1} - {scale.get_notes(key)[fh_hole].name}')

        print(f'----------------------------')

    finally:
        sess.close()


if __name__ == '__main__':
    main()
