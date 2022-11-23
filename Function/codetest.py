productlist = []
orderlist = []
courierlist = []

#ALL MENU
def printing(x, y, z):
    index = 0
    for i in z:
        print(f'{index}: {x} {i[x]} {y} {i[y]}')
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
        z[index_value][y]=b
    return z

def delete(z):
    item_finder = input('Insert the number that you would like to delete: ')
    try:
        item_finder = int(item_finder)
        del z[item_finder]
        return z
    except:
        print('You did not enter a correct value')

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
        print(f"\n[{index}]:, {order['name']}, {order['address']}, {order['courier selection']}, {order['status']}, {order['items']}")
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