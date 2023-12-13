from database.models import Customer, Orders, Flute
from database.connection import get_session
from sqlalchemy import update
from datetime import datetime
import datetime


sess = get_session()


def select_script() -> int:
    """Selects script to run"""
    while True:
        value = input(f'SELECT NUMBER: ')
        if not value:
            break
        try:
            return int(value)
        except ValueError:
            print('Invalid Input')


def update_my_orders(cust_id, first, last):

    while True:
        spacing(10)
        print(f'Customer: {first} {last}')
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

        elif selection == 2:
            update_order(cust_id)

        elif selection == 3:
            update_flute(cust_id)

        elif selection == 4:
            add_flute_to_order(cust_id, first, last)

        elif not selection:
            break


def check_for_customer() -> [int, str, str]:

    cust_id = ''
    cust_list = [()]
    for item in sess.query(Customer).all():
        print(f'({item.id}) {item.first_name} {item.last_name}')
        cust_list.append([item.id, item.first_name, item.last_name])
    cust_id = input('Enter ID Number: ')
    if not cust_id:
        result = [0, 'None', 'None']
    else:
        result = cust_list[int(cust_id)]
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
        defaults = ('', '', '', '', '', 'USA')

        for name in entry_list:
            if not defaults[entry_list.index(name)]:
                if name == 'state' or name == 'country':
                    entries.append(input(f'Enter {name}: ').upper())
                elif name == 'city':
                    entries.append(input(f'Enter {name}: ').capitalize())
                else:
                    entries.append(input(f'Enter {name}: '))
            else:
                entry = input(f'Enter {name} ({defaults[entry_list.index(name)]}): ')
                if not entry:
                    entry = defaults[entry_list.index(name)]
                entries.append(entry)

        sess.add(
            Customer(first_name=first, last_name=last, email=entries[0],
                     address=entries[1], city=entries[2], state=entries[3], postal_code=entries[4], country=entries[5]))

        sess.commit()
    else:
        spacing(1)
        print(f'<<< Customer {first} {last} already exists >>>')


def update_customer(cust_id):

    items = {1: 'first_name', 2: 'last_name', 3: 'email', 4: 'address', 5: 'city', 6: 'state',
             7: 'postal_code', 8: 'country'}

    while True:
        for name in sess.query(Customer).all():
            if name.id == cust_id:
                print('\n____________________________')
                print(f'(1) First Name: {name.first_name}\n(2) Last Name: {name.last_name}'
                      f'\n(3) Email: {name.email}\n(4) Address: {name.address}\n(5) City: {name.city}'
                      f'\n(6) State: {name.state}\n(7) Postal Code: {name.postal_code}\n(8) Country: {name.country}')
                print('____________________________')
        item = input('Select item number to modify: ')
        if not item:
            break
        if item == 1 or item == 3 or item == 5:
            updated_item = input('Enter updated value: ').capitalize()
        elif item == 6 or item == 8:
            updated_item = input('Enter updated value: ').upper()
        else:
            updated_item = input('Enter updated value: ')

        spacing(1)
        u = update(Customer)
        u = u.values({items[int(item)]: updated_item})
        u = u.where(Customer.id == cust_id)
        sess.execute(u)
        sess.commit()


def take_order(cust_id) -> int:

    today = f'{datetime.date.today().month}/{datetime.date.today().day}/{datetime.date.today().year}'
    entries = []
    entry_list = ('order_date', 'total_price', 'discount', 'ship_date')
    defaults = (today, '0.0', '0.0', '')

    for name in entry_list:
        if not defaults[entry_list.index(name)]:
            entries.append(input(f'Enter {name}: '))
        else:
            entry = input(f'Enter {name} ({defaults[entry_list.index(name)]}): ')
            if not entry:
                entry = defaults[entry_list.index(name)]
            entries.append(entry)

    sess.add(Orders(customer_id=cust_id, order_date=entries[0], total_price=entries[1], discount=entries[2],
                    ship_date=entries[3]))

    sess.commit()
    order_id = sess.query(Orders).count()
    return order_id


def update_order(cust_id):

    items = {1: 'id', 2: 'order_date', 3: 'total_price', 4: 'discount', 5: 'ship_date'}
    while True:
        for order in sess.query(Orders).all():
            if order.customer_id == cust_id:
                print(f'(ID: {order.id}) Order Date: {order.order_date}, Total Price: {order.total_price}, '
                      f'Discount: {order.discount}, Date Shipped {order.ship_date}')

        order_id = (input('\nSelect ID number: '))
        if not order_id:
            break

        val = (sess.query(Orders).all()[int(order_id) - 1])

        spacing(1)
        print(f'(2) Order Date: {val.order_date}\n(3) Total Price: {val.total_price}\n(4) Discount: '
              f'{val.discount}\n(5) Date Shipped: {val.ship_date}')

        item = input('\nSelect item number to modify: ')
        if not item:
            break
        updated_item = input('Enter updated value: ')

        spacing(1)
        u = update(Orders)
        u = u.values({items[int(item)]: updated_item})
        u = u.where(Orders.id == order_id)
        sess.execute(u)
        sess.commit()


def create_flute(order_id, cust_id):

    entries = []
    entry_list = ('flute_type', 'hand', 'key', 'octave', 'scale_name', 'tuning_ref', 'flute_wood', 'block_wood')
    defaults = ('Single', '', '4', 'Minor pent', '440', '', '')

    for name in entry_list:
        if not defaults[entry_list.index(name)]:
            entries.append(input(f'Enter {name}: ').capitalize())
        else:
            entry = input(f'Enter {name} ({defaults[entry_list.index(name)]}): ').capitalize()
            if not entry:
                entry = defaults[entry_list.index(name)]
            entries.append(entry)

    sess.add(Flute(order_id=order_id, customer_id=cust_id, flute_type=entries[0], hand=entries[1], key=entries[2],
                   octave=entries[3], scale_name=entries[4], tuning_ref=entries[5], flute_wood=entries[6],
                   block_wood=entries[7]))

    sess.commit()


def update_flute(cust_id):

    items = {1: 'flute_type', 2: 'hand', 3: 'key', 4: 'octave', 5: 'scale_name', 6: 'tuning_ref', 7: 'flute_wood',
             8: 'block_wood'}
    while True:
        for cust in sess.query(Customer).all():
            if cust.id == cust_id:
                print(f'{cust.first_name} {cust.last_name}')

        for name in sess.query(Flute).all():
            if name.customer_id == cust_id:
                print(f'(Order ID: {name.order_id}, Flute ID: {name.id},  Flute Type: {name.flute_type},'
                      f'Key: {name.key}, Octave: {name.octave}, Scale: {name.scale_name}, '
                      f'Tuning Ref: {name.tuning_ref}, Flute Wood: {name.flute_wood}, Block Wood: {name.block_wood}')
        print('-------------------------')
        flute_id = (input('\nSelect FLUTE ID number: '))
        if not flute_id:
            break

        for flute in sess.query(Flute).all():
            if flute.id == int(flute_id):
                print(f'((1) Flute Type: {flute.flute_type}\n(2) Hand: {flute.hand}\n(3) Key: {flute.key}\n'
                      f'(4) Octave: {flute.octave}\n(5) Scale: {flute.scale_name}\n'
                      f'(6) Tuning Ref: {flute.tuning_ref}\n(7) Flute Wood: {flute.flute_wood}\n'
                      f'(8) Block Wood: {flute.block_wood}')
        print('-------------------------')

        item = input('Select item number to modify: ')

        if item == 6 or item == 7:
            updated_item = input('Enter updated value: ')
        else:
            updated_item = input('Enter updated value: ').capitalize()

        if not updated_item:
            break

        spacing(1)
        u = update(Flute)
        u = u.values({items[int(item)]: updated_item})
        u = u.where(Flute.id == flute_id)
        sess.execute(u)
        sess.commit()


def get_customer_id(first, last) -> int:

    cust_id = 0
    for name in sess.query(Customer).all():
        if name.first_name == first and name.last_name == last:
            cust_id = name.id
    return cust_id


def add_flute_to_order(cust_id, first, last):
    print(f'\n{first} {last}: Current Flutes')
    print('--------------------------')
    for flute in sess.query(Flute).join(Orders).filter(Orders.ship_date == '', Orders.customer_id == cust_id):
        print(f'Order ID: {flute.order_id}  Key: {flute.key}  \tOctave: {flute.octave}')
    print('--------------------------\n')
    order_id = input('Select Order ID: ')
    if order_id:
        create_flute(int(order_id), cust_id)


def get_dates():
    check = False
    start = str
    end = str
    while not check:
        try:
            start = datetime.strptime((input('Start date (MM/DD/YY): ')), '%m/%d/%y')
            check = True
        except ValueError:
            print('Invalid input')
            check = False
            continue
        try:
            end = datetime.strptime((input('End date (MM/DD/YY): ')), '%m/%d/%y')
            check = True
        except ValueError:
            check = False
            print('Invalid input')
            continue
    return start, end


def working_order(cust_id, first, last):
    for name in sess.query(Orders).all():
        if name.customer_id == cust_id:
            amount += name.total_price - name.discount
            count += 1
    print(f'({first} {last}) Num Orders: {count}, Total Price: {amount}')
    input('\nPress Enter to continue...')


def view_orders():
    while True:
        spacing(10)
        print('****************************')
        print('1. View Customer Orders    *')
        print('2. View ALL Orders         *')
        print('3. View Not Shipped        *')
        print('****************************')

        selection = select_script()
        spacing(20)
        name = ''
        f_id = ''
        if selection == 1:
            cust_id, first, last = check_for_customer()
            if cust_id == '0':
                break
            spacing(20)
            for item in sess.query(Orders).all():
                for cust in sess.query(Customer).all():
                    if cust.id == item.customer_id:
                        name = f'{cust.first_name} {cust.last_name}'
                        if item.customer_id == cust_id:
                            print(f'({name}) ID: {item.id}, Customer ID: {item.customer_id}, '
                                  f'Order Date: {item.order_date}, Total Price: {item.total_price}, '
                                  f'Discount: {item.discount}, Date Shipped: {item.ship_date}')
                            for flute in sess.query(Flute).all():
                                if flute.customer_id == cust_id:
                                    print(f'ID: {flute.id}, Key: {flute.key}, Type: {flute.flute_type}, '
                                          f'Hand: {flute.hand}, Octave: {flute.octave}, 'f'Scale: {flute.scale_name}, '
                                          f'Tuning Ref: {flute.tuning_ref}, 'f'Body: {flute.flute_wood}, '
                                          f'Block: {flute.block_wood}')
                            f_id = input('\nEnter Flute ID...')
                            if f_id == '':
                                break
                            for flute in sess.query(Flute).all():
                                if flute.id == int(f_id):
                                    print(name)
                                    print('---------------------------------')
                                    print(f'Key: {flute.key}\n, Type: {flute.flute_type}\n, Hand: {flute.hand}\n, '
                                          f'Octave: {flute.octave}\n, 'f'Scale: {flute.scale_name}\n, '
                                          f'uning Ref: {flute.tuning_ref}\n, 'f'Body: {flute.flute_wood}\n, '
                                          f'Block: {flute.block_wood}')
                                    print('_________________________________\n')
            input('Press Enter when done...')

        elif selection == 2:
            for item in sess.query(Orders).all():
                for cust in sess.query(Customer).all():
                    if cust.id == item.customer_id:
                        name = f'{cust.first_name} {cust.last_name}'
                        print(f'({name})\t ID: {item.id}, Customer ID: {item.customer_id}, '
                              f'Order Date: {item.order_date}, Total Price: {item.total_price}, '
                              f'Discount: {item.discount}, Date Shipped: {item.ship_date}')
            input('\nPress Enter to continue...')

        elif selection == 3:

            for item in sess.query(Orders).all():
                for cust in sess.query(Customer).all():
                    if cust.id == item.customer_id:
                        name = f'{cust.first_name} {cust.last_name}'
                if not item.ship_date:
                    print(f'({name})\t ID: {item.id}, Customer ID: {item.customer_id}, Order Date: {item.order_date}, '
                          f'Total Price: {item.total_price}, Discount: {item.discount},'
                          f' Date Shipped: {item.ship_date}')
            input('\nPress Enter to continue...')

        elif not selection:
            break


def view_sales():
    while True:
        spacing(10)
        print('****************************')
        print('1. All Sales               *')
        print('2. Sales By Customer       *')
        print('3. Sales By Year           *')
        print('4. Sales Between Dates     *')
        print('****************************')

        selection = select_script()
        spacing(10)
        amount = 0.0
        count = 0
        if selection == 1:
            spacing(20)
            for name in sess.query(Orders).all():
                amount += name.total_price - name.discount
                count += 1
            print(f'Num Orders: {count}, Total Price: {amount}')
            input('\nPress Enter to continue...')

        elif selection == 2:
            cust_id, first, last = check_for_customer()
            spacing(20)

            for name in sess.query(Orders).all():
                if name.customer_id == cust_id:
                    amount += name.total_price - name.discount
                    count += 1
            print(f'({first} {last}) Num Orders: {count}, Total Price: {amount}')
            input('\nPress Enter to continue...')

        elif selection == 3:
            spacing(20)
            year = input('Enter year (yy): ')
            for name in sess.query(Orders).all():
                if year in name.ship_date:
                    amount += name.total_price - name.discount
                    count += 1
            print(f'Num Orders: {count}, Total Price: {amount}')
            input('\nPress Enter to continue...')

        elif selection == 4:
            spacing(20)
            start, end = get_dates()
            for name in sess.query(Orders).all():
                if start <= datetime.strptime(name.ship_date, '%m/%d/%y') <= end:
                    amount += name.total_price - name.discount

            print(f'Num Orders: {count}, Total Price: {amount}')
            input('\nPress Enter to continue...')

        elif not selection:
            break


def spacing(nums):
    for lines in range(nums):
        print()


def main():

    while True:
        spacing(10)
        print('****************************')
        print('1. Create Customer         *')
        print('2. Create Order            *')
        print('3. Update Order            *')
        print('****************************')

        selection = select_script()
        spacing(1)

        if selection == 1:
            create_customer()

        elif selection == 2:
            cust_id, first, last = check_for_customer()
            order_id = take_order(cust_id)
            create_flute(order_id, cust_id)

        elif selection == 3:
            cust_id, first, last = check_for_customer()
            update_my_orders(cust_id, first, last)

        elif not selection:
            break


if __name__ == '__main__':
    main()
