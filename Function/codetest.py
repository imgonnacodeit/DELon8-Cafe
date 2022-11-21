productlist = []
orders = []
courierlist = []

#ALL MENU
def add(x, z):
    z.append(x)
    return(z)

def delete(z):
    item_finder = input('Insert the number that you would like to delete: ')
    try:
        item_finder = int(item_finder)
        del z[item_finder]
        return z
    except:
        print('You did not enter a correct value')

#PRODUCTS ONLY MENU
def PRODUCT_create_new():
    new_addition = input('Please enter the new item that you need.')
    new_addition = new_addition.lower()
    if new_addition != '':
        return new_addition
    else:
        print('You cannot have an empty value.\n Please start again')
    
def PRODUCT_createPrice():
    new_price = input('What is the price of the item?: ')
    try:
        float(new_price)
        return new_price
    except:
        print('This entry is not valid please start again')
   
def PRODUCT_dic():
    diction = {'name': PRODUCT_create_new(), 'price': PRODUCT_createPrice()}
    return diction

def PRODUCT_printing(x, y, z):
    index = 0
    for i in z:
        print(f'{index}: {x} {i[x]} {y} {i[y]}')
        index = index + 1

def PRODUCT_update(w, x, y, z): 
    z[w][x] = y
    return z

#COURIERS ONLY MENU
def COURIER_printing(z):
    index = 0
    for i in z:
        print(f'{index}: {i}')
        index = index + 1

def COURIER_update(x, y, z):
    z[x] = y
    return z


#PERSISTING DATA MENU
