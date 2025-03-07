import pytest
from bank import value

def test_value():
    assert value("Hello there") == 0
    assert value("hi there") == 20
    assert value("sure") == 100
    assert value("") == 100
    assert value("123") == 100


