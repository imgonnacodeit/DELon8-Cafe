import codetest
import requests
from unittest.mock import Mock
from unittest.mock import patch


# TESTS CREATE NEW
#***********************************************
#Checking if my input patch works.
@patch('builtins.input')
def test_createNew(mock_input):
    mock_input.return_value = 'fanta'
    result = codetest.createNew()
    assert(result == 'fanta')
    assert mock_input.call_count == 1

# Checking the patch works with capital letters. 
@patch('builtins.input')
def test_createNew_caps(mock_input):
    mock_input.return_value = 'ceREAl'

    result = codetest.createNew()

    assert(result == 'cereal')
    assert mock_input.call_count == 1


#Making sure that the input cannot be empty
@patch('builtins.input')
def test_createNew_none(mock_input):
    mock_input.return_value = ''
    result = codetest.createNew()
    assert result == 'You cannot have an empty value.'
    assert mock_input.call_count == 1

#Making sure that the inputs are a string. 
@patch('builtins.input')
def test_createNew_string(mock_input):
    mock_input.return_value = 'cOke'

    result = codetest.createNew()

    assert (isinstance(result, str))
    assert mock_input.call_count == 1

# # capture something printed to screen
# def test_print_things(capsys):
#     stdout, stderr = capsys.readouterr()
#     assert stdout == 'hi\n'



# CREATE PRICE
#*********************************************
#Inserting an integer
@patch('builtins.input')
def test_PRODUCT_createPrice_integer(mock_input):
    mock_input.return_value = 2
    result = codetest.PRODUCT_createPrice()
    assert (result == 2)
    assert mock_input.call_count == 1

#Inserting a float
@patch('builtins.input')
def test_PRODUCT_createPrice_integer(mock_input):
    mock_input.return_value = 2.56
    result = codetest.PRODUCT_createPrice()
    assert (result == 2.56)
    assert mock_input.call_count == 1

#Inserting a string
@patch('builtins.input')
def test_PRODUCT_createPrice_string(mock_input):
    mock_input.return_value = 'fantastic'
    result = codetest.PRODUCT_createPrice()
    assert (result == 'This is not a number please start again.')
    assert mock_input.call_count == 1










# #TEST TO ADD SOMETHING TO A LIST
# #*******************************************
# '''The append functoin is called here and therefore does not need
# testing for it as it is called in a single line.'''

# #TEST TO VIEW ALL PRODUCTS
# #******************************************
# '''This can be done in a nicer way later but it is not a core requirment at this stage'''


# #TDD-TEST TO WRITE CODE TO UPDATE THE ORDER VALUES
# #1. Print the orders list with index values.
# def test_update_order():
#     pass
