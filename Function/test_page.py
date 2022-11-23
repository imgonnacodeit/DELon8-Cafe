import codetest
import requests
import requests_mock
from unittest.mock import Mock
from unittest.mock import patch
import pytest
#Types of tests
#COMMON CASE - Normal operating parameters
#EDGE CASE - Occurs at the extreme values
#CORNER CASE - Occurs outside of normal parameters

#How to create a test.
#Assemble - Arrange what I am going to test
#Act - Call the function with the parameters 
#Assert - Write an assertion so that it can fail then pass.

#create a product - DONE
#add product to list - DONE
#view all products - DONE
#update a product - DONE
#delete a product - DONE


#*********************************************************PRODUCTS************************************************************************************

# TESTS CREATE NEW
#***********************************************
# Checking if my input patch works in the pytest.
@patch('builtins.input')
def test_PRODUCT_create_new_happy(mock_input):
    mock_input.return_value = 'fanta'
    x = 'of the item'
    result = codetest.create_new(x)
    assert(result == 'fanta')
    assert mock_input.call_count == 1

# Checking the patch works with capital letters. 
@patch('builtins.input')
def test_PRODUCT_create_new_happy_caps(mock_input):
    mock_input.return_value = 'ceREAl'
    x = 'of the item'
    result = codetest.create_new(x)
    assert(result == 'cereal')
    assert mock_input.call_count == 1

#Making sure that the inputs are in a string format. 
@patch('builtins.input')
def test_PRODUCT_create_new_string(mock_input):
    mock_input.return_value = 'cOke'
    x = 'of the item'
    result = codetest.create_new(x)
    assert (isinstance(result, str))
    assert mock_input.call_count == 1


# CREATE PRICE
#*********************************************
# Checking to see if function would take an integer 
@patch('builtins.input')
def test_createPrice_happy_integer_input(mock_input):
    mock_input.return_value = 10
    result = codetest.PRODUCT_createPrice()
    assert result == 10

#Checking to see if it would take a float as an input
@patch('builtins.input')
def test_createPrice_happy_floating_input(mock_input):
    mock_input.return_value = 54.23
    result = codetest.PRODUCT_createPrice()
    assert result == 54.23

#Checking to see if it would take a float as an input
@patch('builtins.input')
def test_createPrice_happy_edge_case(mock_input):
    mock_input.return_value = 546544.24646546546543
    result = codetest.PRODUCT_createPrice()
    assert result == 546544.24646546546543


#Should output a floating number type.
@patch('builtins.input')
def test_createPrice_happy_type(mock_input):
    mock_input.return_value = 54.23
    result = codetest.PRODUCT_createPrice()
    assert isinstance(result, float)


#Should not accept a string and raise and error. 
#This test passed until I coded the exception. 
@pytest.mark.skip(reason ='This has been handled by another test so it has been skipped intentionally')
@patch('builtins.input')
def test_createPrice_unhappy_type(mock_input):
    with pytest.raises(ValueError):
        mock_input.return_value = 'fancy'
        result = codetest.PRODUCT_createPrice()


#Should pass through the exception block
@patch('builtins.input')
def test_createPrice_unhappy_type_exception(mock_input, capsys):
    mock_input.return_value = 'flirt'
    codetest.PRODUCT_createPrice()
    stdout, stderr = capsys.readouterr()
    assert stdout == 'This entry is not valid please start again\n'


#TEST TO ADD SOMETHING TO A LIST
#This was the only test required as the dependencies have also been tested.
#*******************************************
def test_PRODUCT_add_happy_case():
    expected = [{'name': 'apple', 'price': 0.65}]
    z = []
    diction = {'name': 'apple', 'price': 0.65}
    actual = codetest.add(diction, z)
    assert actual == expected



#TEST TO VIEW ALL THE PRODUCTS 
#The test shows that the products inserted are printed to the console 
#*******************************************
def test_PRODUCT_print_happy_case(capsys):
    expected = '0: name apple, price 0.65\n'
    x = 'name'
    y = 'price'
    z = [{'name': 'apple','price': 0.65}]
    actual = codetest.printing(x, y, z)
    stdout, stderr = capsys.readouterr()
    assert stdout == expected


#TEST TO UPDATE PRODUCTS
#***********************
def test_update_happy_name():
    index_value = 1
    a = 'oats'
    b = ''
    x = 'name'
    y = 'price'
    z = [{'name': 'apple', 'price': 0.65}, {'name': 'juice', 'price': 2.54}]
    expected = [{'name': 'apple', 'price': 0.65}, {'name': 'oats', 'price': 2.54}]
    actual = codetest.update(index_value, a, b, x, y, z)
    assert expected == actual

def test_update_happy_price():
    index_value = 1
    a = ''
    b = 0.99
    x = 'name'
    y = 'price'
    z = [{'name': 'apple', 'price': 0.65}, {'name': 'juice', 'price': 2.54}]
    expected = [{'name': 'apple', 'price': 0.65}, {'name': 'juice', 'price': 0.99}]
    actual = codetest.update(index_value, a, b, x, y, z)
    assert expected == actual

def test_update_edge_price_nothing():
    index_value = 1
    a = ''
    b = ''
    x = 'name'
    y = 'price'
    z = [{'name': 'apple', 'price': 0.65}, {'name': 'juice', 'price': 2.54}]
    expected = [{'name': 'apple', 'price': 0.65}, {'name': 'juice', 'price': 2.54}]
    actual = codetest.update(index_value, a, b, x, y, z)
    assert expected == actual

def test_update_edge_both_changed_happy():
    index_value = 1
    a = 'cherry'
    b = 0.74
    x = 'name'
    y = 'price'
    z = [{'name': 'apple', 'price': 0.65}, {'name': 'juice', 'price': 2.54}]
    expected = [{'name': 'apple', 'price': 0.65}, {'name': 'cherry', 'price': 0.74}]
    actual = codetest.update(index_value, a, b, x, y, z)
    assert expected == actual

def test_update_edge_string_in_price_unhappy(capsys):
    index_value = 1
    a = ''
    b = 'fancy'
    x = 'name'
    y = 'price'
    z = [{'name': 'apple', 'price': 0.65}, {'name': 'juice', 'price': 2.54}]
    expected = 'The value that you have entred is not a number please enter a numerical value. Please start again.\n'
    actual = codetest.update(index_value, a, b, x, y, z)
    stdout, stderr = capsys.readouterr()
    assert stdout == expected


#TEST TO DELETE 
#**************************
#Delete the item
@patch('builtins.input')
def test_PRODUCT_delete_happy(mock_input, capsys):
    mock_input.return_value = 0
    list = [{'name': 'apple', 'price': 0.65}, {'name': 'berries', 'price': 1.05}]
    actual = codetest.delete(list)
    result = [{'name': 'berries', 'price': 1.05}]
    assert actual == result

#Cannot delete if a string is put in
@patch('builtins.input')
def test_PRODUCT_delete_unhappy_string(mock_input, capsys):
    mock_input.return_value = 'between'
    list = [{'name': 'apple', 'price': 0.65}, {'name': 'berries', 'price': 1.05}]
    codetest.delete(list)
    stdout, stderr = capsys.readouterr()
    assert stdout == 'You did not enter a correct value. Please start again.\n'

#TEST ORDERS MENU
#*************************
