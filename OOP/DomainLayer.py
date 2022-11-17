class Product:
    def __init__(self, name):
        '''This creates a name for the product.'''
        self.name = name
    
    def __str__(self):
        return f'{self.name}'

class ProductList:
    def __init__(self):
        '''This is the blueprint that carrys all of the products.'''
        self.productlist = []

    def __iter__(self):
        '''This allows the list to be iterated over.'''
        yield from self.productlist

    def add_product(self, product):
        '''This allows me to add a product to the list.'''
        self.productlist.append(product)
    
    def delete_product(self, index):
        '''This allows me to remove a product from the list.'''
        self.productlist.pop[index]
    
    def update_product(self, index):
        '''This allows me to update a product'''
        pass



























#     def update_product(self, index, name):
#         # product = self.productlist.pop(index)
#         # product.name = name
#         # self.productlist.append(name)
#         #this only has one responsibility 
#         self.productlist[index].name = name
