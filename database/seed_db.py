import csv

from database.models import Note, Scale, ScaleOffset, Base, FHP
from database.connection import get_session, get_engine


Base.metadata.drop_all(get_engine())
Base.metadata.create_all(get_engine())

session = get_session()

notes = [
    Note(name='A', offset=0),
    Note(name='A#', offset=1),
    Note(name='B', offset=2),
    Note(name='C', offset=3),
    Note(name='C#', offset=4),
    Note(name='D', offset=5),
    Note(name='D#', offset=6),
    Note(name='E', offset=7),
    Note(name='F', offset=8),
    Note(name='F#', offset=9),
    Note(name='G', offset=10),
    Note(name='G#', offset=11),
]

for note in notes:
    session.add(note)

with open('database/scales.csv') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        scale = Scale(name=line[0])
        session.add(scale)

        for offset_val in line[1:]:
            session.add(ScaleOffset(scale=scale, offset=int(offset_val)))

with open('database/fh_percents.csv') as csv_file:
    reader = csv.reader(csv_file)
    for col in reader:
        session.add(FHP(key=col[1], octave=col[2], scale=col[3], fh_1=col[4],fh_2=col[5],fh_3=col[6],fh_4=col[7],
                     fh_5=col[8], fh_6=col[9], fh_7=col[10]))


session.commit()
