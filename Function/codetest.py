productlist = []
orders = []
courierlist = []


def createNew():
    new_addition = input('Please enter the name: ')
    new_addition = new_addition.lower()
    if new_addition == '':
        print('You cannot have an empty value.')
    else:
        return new_addition

def PRODUCT_createPrice():
    new_price = int(input('What is the price of the item?: '))
    return new_price

def PRODUCT_dic():
    diction = {'name': createNew(), 'price': PRODUCT_createPrice()}
    return diction

def PRODUCT_add(x):
    productlist.append(x)

def PRODUCT_print():
    index = 0
    for product in productlist:
        print(index, ': Product:', product['name'], 'Price:', product['price'])
        index += 1

def PRODUCT_update():
    PRODUCT_print()
    to_amend = int(input('Which item number would you like to change?: '))
    name_or_price = int(input('Would you like to change. Select [1]Name or [2]Price: '))
    if name_or_price == 1:
        name_or_price = 'name'
        amended_item = createNew()
    elif name_or_price == 2:
        name_or_price ='price'
        amended_item = PRODUCT_createPrice()
    productlist[to_amend][name_or_price] = amended_item            
    PRODUCT_print()

def PRODUCT_delete():
    PRODUCT_print()
    item_finder = int(input('Insert the item number that you would like to delete: '))
    del productlist[item_finder]
    print ('Your item has been deleted.')
    PRODUCT_print()






# def COURIER_createPhone_number():
#     new_number = int(input('What is the price of the item? '))
#     return new_number

# def COURIER_dic():
#     dic = {'name': createNew(), 'phone number': COURIER_createPhone_number()}
#     return dic
