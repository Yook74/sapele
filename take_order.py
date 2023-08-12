from database.models import Customer, Orders, Flute
from database.connection import get_session
from sqlalchemy import update

sess = get_session()


def select_script() -> int:
    """Selects script to run"""
    while True:
        value = input(f'SELECT NUMBER: ')
        if not value:
            exit()

        try:
            return int(value)
        except ValueError:
            print('Invalid Input')


def update_my_orders(cust_id):

    while True:
        spacing(10)
        print()
        print('****************************')
        print('1. Update Customer         *')
        print('2. Update Order            *')
        print('3. Update Flute            *')
        print('4. Add Flute               *')
        print('****************************')

        spacing(1)

        selection = select_script()

        if selection == 1:
            update_customer(cust_id)

        if selection == 2:
            update_order(cust_id)

        if selection == 3:
            update_flute(cust_id)

        if selection == 4:
            add_flute_to_order(cust_id)


def check_for_customer() -> [bool, int]:

    done = False
    cust_id = 0
    customer_found = True
    while not done:
        first = input('\nEnter First Name: ').capitalize()
        if not first:
            break
        last = input('Enter Last Name: ').capitalize()
        cust_id = get_customer_id(first, last)
        if cust_id:
            customer_found = True
            done = True
        else:
            customer_found = False
            print(' !!! No customer found !!!')
    result = [customer_found, cust_id]
    return result


def create_customer():

    done = False
    first = str
    last = str
    while not done:
        first = input('\nEnter First Name: ').capitalize()
        if not first:
            break
        last = input('Enter Last Name: ').capitalize()
        done = True

    cust_id = get_customer_id(first, last)

    if not cust_id:
        entries = []
        entry_list = ('email', 'address', 'city', 'state', 'postal_code', 'country')

        for name in entry_list:
            entries.append(input(f'Enter {name}: ').capitalize())

        sess.add(
            Customer(first_name=first, last_name=last, email=entries[0],
                     address=entries[1], city=entries[2], state=entries[3], postal_code=entries[4], country=entries[5])
                 )

        sess.commit()
    else:
        spacing(1)
        print(f'<<< Customer {first} {last} already exists >>>')


def get_customer_id(first, last) -> int:

    cust_id = 0
    for name in sess.query(Customer).all():
        if name.first_name == first and name.last_name == last:
            cust_id = name.id
    return cust_id


def take_order(cust_id) -> int:

    entries = []
    entry_list = ('order_date', 'total_price', 'discount', 'ship_date')

    for name in entry_list:
        entry = input(f'Enter {name}: ')
        while not entry:
            print('Entry cannot be Null!')
            entry = input(f'Enter {name}: ')
        entries.append(entry)

    sess.add(Orders(customer_id=cust_id, order_date=entries[0], total_price=entries[1], discount=entries[2],
             ship_date=entries[3]))

    sess.commit()
    order_id = sess.query(Orders).count()
    return order_id


def flute(order_id, cust_id):

    entries = []
    entry_list = ('flute_type', 'key', 'octave', 'scale_name', 'tuning_ref', 'flute_wood', 'block_wood')

    for name in entry_list:
        entries.append(input(f'Enter {name}: ').capitalize())

    sess.add(Flute(order_id=order_id, customer_id=cust_id, flute_type=entries[0], key=entries[1], octave=entries[2],
                   scale_name=entries[3], tuning_ref=entries[4], flute_wood=entries[5], block_wood=entries[6]))

    sess.commit()


def update_order(cust_id):

    items = {1: 'id', 2: 'customer_id', 3: 'order_date', 4: 'total_price', 5: 'discount', 6: 'ship_date'}
    while True:
        for order in sess.query(Orders).all():
            if order.customer_id == cust_id:
                print(f' ID: {order.id}, Order Date: {order.order_date}, Total Price: {order.total_price}, '
                      f'Discount: {order.discount}, Date Shipped {order.ship_date}')

        order_id = (input('\nSelect ID number: '))
        if not order_id:
            break
        val = (sess.query(Orders).all()[int(order_id) - 1])

        spacing(1)
        print(f'(3) Order Date: {val.order_date}, (4) Total Price: {val.total_price}, (5) Discount: '
              f'{val.discount}, (6) Date Shipped {val.ship_date}')

        item = int(input('\nSelect item number to modify: '))
        updated_item = input('Enter updated value: ')

        spacing(1)
        u = update(Orders)
        u = u.values({items[item]: updated_item})
        u = u.where(Orders.id == order_id)
        sess.execute(u)
        sess.commit()


def update_customer(cust_id):

    items = {1: 'id', 2: 'first_name', 3: 'last_name', 4: 'email', 5: 'address', 6: 'state', 7: 'postal_code',
             8: 'country'}
    for name in sess.query(Customer).all():
        if name.id == cust_id:
            print(f'(1) {name.id}, (2) {name.first_name}, (3) {name.last_name},'
                  f' (4) {name.email}, (5) {name.address}, (6) {name.state},'
                  f' (7) {name.postal_code}, (8) {name.country}')

    while True:
        item = input('Select item number to modify: ')
        if not item:
            break
        updated_item = input('Enter updated value: ').capitalize()
        spacing(1)
        u = update(Customer)
        u = u.values({items[int(item)]: updated_item})
        u = u.where(Customer.id == cust_id)
        sess.execute(u)
        sess.commit()


def update_flute(cust_id):

    items = {2: 'flute_type', 3: 'key', 4: 'octave', 5: 'scale_name', 6: 'tuning_ref', 7: 'flute_wood',
             8: 'block_wood'}

    for name in sess.query(Flute).all():
        if name.id == cust_id:
            print(f'(2) {name.flute_type}, (3) {name.key},(4) {name.octave}, (5) {name.scale_name}, '
                  f'(6) {name.tuning_ref}, (7) {name.flute_wood}')

    while True:
        item = input('Select item number to modify: ')
        if not item:
            break
        updated_item = input('Enter updated value: ').capitalize()
        spacing(1)
        u = update(Flute)
        u = u.values({items[int(item)]: updated_item})
        u = u.where(Flute.id == cust_id)
        sess.execute(u)
        sess.commit()


def add_flute_to_order(cust_id):

    print('\n--------------------------')
    for order in sess.query(Orders).all():
        if order.customer_id == cust_id:
            print(f'ID: {order.id} \tDate: {order.order_date}')
    print('--------------------------\n')
    order_id = int(input('Select ID: '))
    flute(order_id, cust_id)


def spacing(nums):
    for lines in range(nums):
        print()


def main():

    while True:
        spacing(2)
        print('****************************')
        print('1. Create Customer         *')
        print('2. Create Order            *')
        print('3. Update Order            *')
        print('****************************')

        spacing(1)

        num_select = select_script()

        if num_select == 1:
            create_customer()

        if num_select == 2:
            customer_found, cust_id = check_for_customer()
            if customer_found:
                order_id = take_order(cust_id)
                flute(order_id, cust_id)

        if num_select == 3:
            customer_found, cust_id = check_for_customer()
            if customer_found:
                update_my_orders(cust_id)


if __name__ == '__main__':
    main()




