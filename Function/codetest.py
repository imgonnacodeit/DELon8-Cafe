productlist = []
orderlist = []
courierlist = [] 

import csv

#Reading from a file
def opening_products(t):
    with open('products.csv', 'r') as file:
        csv_file = csv.DictReader(file, delimiter=',')
        for row in csv_file:
            t.append(row)

def opening_couriers(r):
    with open('couriers.csv', 'r') as file:
        csv_file = csv.DictReader(file, delimiter=',')
        for row in csv_file:
            r.append(row)

def opening_orders(s):
   with open('orders.csv', 'r') as file:
        csv_file = csv.DictReader(file, delimiter=',')
        for row in csv_file:
            s.append(row)

#Writing to file 
def writer_product(z):
    with open('products.csv', mode='w') as file:
        fieldnames = ['name', 'price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for i in z:
            writer.writerow(i)

def writer_courier(z):
    with open('couriers.csv', mode='w') as file:
        fieldnames = ['name', 'phone number']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for i in z:
            writer.writerow(i)

def writer_order(cl):
    with open('orders.csv', mode='w') as file:
        fieldnames = ['name', 'address', 'phone number', 'courier selection', 'status', 'items']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for i in cl:
            writer.writerow(i)

#ALL MENU
def printing(x, y, z):
    index = 0
    for i in z:
        print(f'{index}: {x} {i[x]}, {y} {i[y]}')
        index = index + 1

def add(x, z):
    z.append(x)
    return(z)

def update(index_value, a, b, x, y, z): 
    if a == '':
        pass
    elif a != '':
        z[index_value][x]=a
                    
    if b=='':
        pass
    elif b !='':
        try:
            float(b)
            z[index_value][y]=b
        except:
            print('The value that you have entred is not a number please enter a numerical value. Please start again.')
    return z

def delete(z):
    item_finder = input('Insert the number that you would like to delete: ')
    try:
        item_finder = int(item_finder)
        del z[item_finder]
        return z
    except:
        print('You did not enter a correct value. Please start again.')

def create_new(x):
    new_addition = input(f'Please enter the new name {x} that you need.')
    new_addition = new_addition.lower()
    if new_addition != '':
        return new_addition
    else:
        print('You cannot have an empty value.\n Please start again')

#PRODUCTS ONLY MENU   
def PRODUCT_createPrice():
    new_price = input('What is the price of the item?: ')
    try:
        float(new_price)
        price = ()
        return new_price
    except:
        print('This entry is not valid please start again')

def PRODUCT_making_dic(x):
    diction = {'name': create_new(x), 'price': PRODUCT_createPrice()}
    return diction

#COURIERS ONLY MENU 
def COURIER_create_Phonenumber():
    new_phonenumber = input('What is the phonenumber of the person?: ')
    try:
        int(new_phonenumber)
        return new_phonenumber
    except:
        print('This entry is not valid please start again')

def COURIER_making_dic(x):
    diction = {'name': create_new(x), 'phone number': COURIER_create_Phonenumber()}
    return diction


#ORDERS ONLY MENU
def ORDER_dic(customer_name, customer_address, customer_phone, courier_selection, status, product_selection):
    order_diction = {'name': customer_name, 'address': customer_address, 'phone number': customer_phone, 'courier selection': courier_selection,  'status': status, 'items': product_selection }
    return order_diction

def ORDER_print(cl):
    index = 0
    for order in cl:
        print(f"\n[{index}]: {order['name']}, {order['address']}, {order['courier selection']}, {order['status']} {order['items']}")
        index = index + 1

def ORDER_update(index_value, a, b, c, d, cl): 
    if a == '':
        pass
    elif a != '':
        cl[index_value]['name']=a
                    
    if b=='':
        pass
    elif b !='':
        cl[index_value]['address']=b

    if c == '':
        pass
    elif c != '':
        cl[index_value]['courier selection']=c

    if d == '':
        pass
    elif d != '':
        cl[index_value]['items']=d

    return cl

def ORDER_status_update(selection, ol):
    order_status = ['Preparing', 'Ready', 'Out for delivery']
    choice = int(input('Please select which status you would like to update the order to.\n[0] Preparing\n[1] Ready\n[2] Out for delivery\n'))
    if choice != '':
        ol[selection]['status'] = order_status[choice]

def ORDER_status_print_list(ol):
    index = 0
    for i in ol:
        print(f"Order [{index}] status is {i['status']}")
        index += 1

def ordering_ORDERS(change_order, ol):
    if change_order == 0:
        done = (sorted(ol, key=lambda q: q['status']))
        return done
    
    elif change_order == 1:
        done = (sorted(ol, key=lambda q: q['courier selection']))
        return done