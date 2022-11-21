productlist = []
orders = []
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

def update(w, x, y, z): 
    z[w][x] = y
    return z

def delete(z):
    item_finder = input('Insert the number that you would like to delete: ')
    try:
        item_finder = int(item_finder)
        del z[item_finder]
        return z
    except:
        print('You did not enter a correct value')


def create_new():
    new_addition = input(f'Please enter the new value that you need.')
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

def PRODUCT_making_dic():
    diction = {'name': create_new(), 'price': PRODUCT_createPrice()}
    return diction

#COURIERS ONLY MENU 
def COURIER_create_Phonenumber():
    new_phonenumber = input('What is the price of the item?: ')
    try:
        int(new_phonenumber)
        return new_phonenumber
    except:
        print('This entry is not valid please start again')

def COURIER_making_dic():
    diction = {'name': create_new(), 'price': COURIER_create_Phonenumber()}
    return diction