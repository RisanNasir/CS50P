import pytest
from jar import Jar

jar = Jar()

def test_init():

    with pytest.raises(ValueError):
        jar1 = Jar(-5)
        

def test_str():

    assert str(jar) == ""


def test_deposit():

    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    with pytest.raises(ValueError):
        jar.deposit(10)

def test_withdraw():

    jar.withdraw(1)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"

    with pytest.raises(ValueError):
        jar.withdraw(7)
