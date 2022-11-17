#This class contains the products.
class Product:
    #This method creates the product object.
    def __init__(self, name):
        self.name = name




#This class contains the product list.
class ProductList:
    def __init__(self):
        '''This creates an empty list to append items to'''
        self.productlist = []
        

    def add_product(self, product: Product):
        '''This method takes the items and adds it to a list'''
        self.productlist.append(product)
        
    
    def delete_product(self, index):
        '''This method deletes the product'''
        self.productlist.remove(index)

    def update_product(self, index, name):
        # product = self.productlist.pop(index)
        # product.name = name
        # self.productlist.append(name)
        #this only has one responsibility 
        self.productlist[index].name = name
