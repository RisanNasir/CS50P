import pytest
from um import count

def test_1():
    assert count("um, Hello, um.") == 2


def test_2():
    assert count("UM?") == 1


def test_3():

    assert count("hi there, um Um. uM, Um.") == 4
    assert count("Hello thanks for UMbrella and album") == 0
