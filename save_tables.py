from database.connection import get_session
import pandas as pd
import time


sess = get_session()
conn = sess.connection()


def main():
    print('\n<<< Saving FHP table to database/fh_percents.csv >>>')
    df = pd.read_sql('SELECT * from FHP', conn)
    df.to_csv('database/fh_percents.csv', index=False, header=True)
    time.sleep(.5)

    print('<<< Saving Customer table to database/customers.csv >>>')
    df = pd.read_sql('SELECT * from Customer', conn)
    df.to_csv('database/customers.csv', index=False, header=True)
    time.sleep(.5)

    print('<<< Saving Orders table to database/orders.csv >>>')
    df = pd.read_sql('SELECT * from Orders', conn)
    df.to_csv('database/orders.csv', index=False, header=True)
    time.sleep(.5)

    print('<<< Saving Flutes table to database/flute.csv >>>')
    df = pd.read_sql('SELECT * from Flute', conn)
    df.to_csv('database/flute.csv', index=False, header=True)
    time.sleep(.5)


if __name__ == '__main__':
    main()
