import pytest
from numb3rs import validate

def test_validate():
    assert validate("1.1.1.1") == True
    assert validate("1.255.0.76") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("0.256.275.6") == False
    assert validate("lion") == False
