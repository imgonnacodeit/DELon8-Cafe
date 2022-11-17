from DomainLayer import Product
from DomainLayer import ProductList


#main menu
option = int(input('What is your choice: '))
mylist = ProductList()

if option == 1:
    for product in mylist:
        print(product)
