import csv
from database.models import Note, Scale, ScaleOffset, Base, FHP
from database.connection import get_session, get_engine


sess = get_session()



with open('database/fh_percents.csv') as csv_file:
    reader = csv.reader(csv_file)
    for col in reader:
        sess.add(FHP(key=col[0], octave=col[1], scale=col[2], fh_1=col[3],fh_2=col[4],fh_3=col[5],fh_4=col[6],
                     fh_5=col[7], fh_6=col[8], fh_7=col[9]))

sess.commit()