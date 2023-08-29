from typing import Tuple

from database.models import Customer, Orders, Flute
from database.connection import get_session
from sqlalchemy import update, select
from datetime import datetime, date, time
sess = get_session()

count = 0
amount = 0.0
cust_id = 1

for flute in sess.query(Flute).join(Orders).filter(Orders.ship_date == '', Orders.customer_id == cust_id):
    print(f'Order ID: {flute.order_id}  Key: {flute.key}  \tOctave: {flute.octave}')

#
# def get_dates() -> Tuple[datetime, datetime]:
#     check = False
#     start = str
#     end = str
#     while not check:
#         try:
#             start = datetime.strptime((input('Start date (YYYY-MM-DD): ')), '%m/%d/%y')
#             check = True
#         except ValueError:
#             print('Invalid input')
#             check = False
#             continue
#         try:
#             end = datetime.strptime((input('End date (YYYY-MM-DD): ')), '%m/%d/%y')
#             check = True
#         except ValueError:
#             check = False
#             print('Invalid input')
#             continue
#     return start, end


# start, end = get_dates()


# for name in sess.query(Orders).all():
#     if start <= datetime.strptime(name.ship_date, '%m/%d/%y')  <= end:
#         amount += name.total_price - name.discount
#
# print(f'Num Orders: {count}, Total Price: {amount}')
# input('\nPress Enter to continue...')