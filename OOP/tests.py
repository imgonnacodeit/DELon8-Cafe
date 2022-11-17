from DomainLayer import Product
from DomainLayer import ProductList
from unittest import TestCase
import pytest

#These tests are testing the Product Class.
def test_creating_product():
    apple = Product('apple')
    assert str(apple) == 'apple'

#This test is testing the ProductList Class and methods.
def test_add_one_product():
    object = 'random'
    random = Product('random')
    mylist = ProductList()
    mylist.add_product(random)
    for product in mylist:
        print(product)
    assert str(product) == object

# def test_delete_one_product():
random = Product('random')
mylist = ProductList()
mylist.add_product(random)
for count, value in enumerate(mylist):
    print(count, value)
    master = int(input('What number do you want to select?: '))
    
    # assert len(mylit) == 0

# mylist1 = ProductList
# print(dir(mylist1))