import codetest
from unittest.mock import Mock
from unittest.mock import patch


def test_capital_case():
    mock = 'coke'
    assert codetest.createNew(mock) == 'coke'

def test_adding_to_dict():
    assert codetest.createNew('') == 'You cannot have an empty value.'
