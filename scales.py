from database.models import Note, Scale
from database.connection import get_session

sess = get_session()


def get_key() -> Note:
    while True:
        name = input('Enter a key (for example, C#): ')

        try:
            return Note.from_name(sess, name)
        except ValueError:
            print('Invalid key name')


def get_scale() -> Scale:
    for scale in sess.query(Scale).all():
        print(f'{scale.id}: {scale.name}')

    while True:
        scale_id = input('Please enter the number of a scale: ')
        try:
            scale_id = int(scale_id)
        except ValueError:
            print('Invalid input')

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
