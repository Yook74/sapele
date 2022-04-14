from database.models import Note, Scale
from database.connection import get_session

sess = get_session()


def get_key() -> Note:
    """Allows the user to enter a note which will be the key of the scale"""
    while True:
        name = input('Enter a key (for example, C#): ')

        try:
            return Note.from_name(sess, name)
        except ValueError:
            print('Invalid key name')


def get_scale() -> Scale:
    """Allows the user to choose a scale from the database and returns which scale they chose"""
    for scale in sess.query(Scale).all():
        print(f'{scale.id}: {scale.name}')

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


try:
    while True:
        key = get_key()
        scale = get_scale()

        print(
            ', '.join([note.name for note in scale.get_notes(key)])
            )

finally:
    sess.close()

