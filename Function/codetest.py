productlist = []
orders = []
courierlist = []


def createNew():
    new_addition = input('Please enter the name')
    new_addition = new_addition.lower()
    if new_addition == '':
        print('You cannot have an empty value.')
    else:
        return new_addition

def PRODUCT_createPrice():
    new_price = int(input('What is the price of the item? '))
    return new_price


def PRODUCT_dic():
    diction = {'name': createNew(), 'price': PRODUCT_createPrice()}
    return diction
    
def PRODUCT_add_to_list():
    productlist.append(PRODUCT_dic())


# def COURIER_createPhone_number():
#     new_number = int(input('What is the price of the item? '))
#     return new_number

# def COURIER_dic():
#     dic = {'name': createNew(), 'phone number': COURIER_createPhone_number()}
#     return dic

# def COURIER_add_to_list():
#     courierlist.append(COURIER_dic)