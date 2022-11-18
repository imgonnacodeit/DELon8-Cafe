productlist = []
orders = []
courierlist = []


def createNew():
    new_addition = input('Please enter the new thing that you need.')
    new_addition = new_addition.lower()
    if new_addition == '':
        error = ('You cannot have an empty value.')
        print(error)
        return error
    else:
        return new_addition

def PRODUCT_createPrice():
    try:
        new_price = float(input('What is the price of the item?: '))
        return new_price
    except:
        print('This is not a number please start again.')
   

def PRODUCT_dic():
    diction = {'name': createNew(), 'price': PRODUCT_createPrice()}
    return diction

def PRODUCT_add(x):
    productlist.append(x)
    return(productlist)

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