from database.connection import get_session
import pandas as pd
import time


sess = get_session()
conn = sess.connection()


def main():
    print('\n<<< Saving FHP table to database/fh_percents.csv >>>\n')
    df = pd.read_sql('SELECT * from FHP', conn)
    df. to_csv('database/fh_percents.csv', index=False, header=False)
    time.sleep(2)


if __name__ == '__main__':
   main()