productlist = []
orders = []
courierlist = []


def createNew():
    new_addition = input('Please enter the new thing that you need.')
    new_addition = new_addition.lower()
    while new_addition == '':
        new_addition = input('You cannot have an empty value.\n Please enter the new value for the product')
    return new_addition

def PRODUCT_print(x, y, z):
    index = 0
    for i in z:
        print(f'{index}: {x} {i[x]} {y} {i[y]}')
        index += 1

def PRODUCT_createPrice():
    new_price = input('What is the price of the item?: ')
    try:
        float(new_price)
        return new_price
    except:
        print('This entry is not valid please start again')
   
def PRODUCT_dic():
    diction = {'name': createNew(), 'price': PRODUCT_createPrice()}
    return diction

def PRODUCT_add(x):
    productlist.append(x)
    return(productlist)

def PRODUCT_update():
    pass     

def PRODUCT_delete(z):
    item_finder = int(input('Insert the item number that you would like to delete: '))
    del z[item_finder]
    print (z)