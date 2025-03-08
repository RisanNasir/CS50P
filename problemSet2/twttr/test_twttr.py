import pytest
from twttr import shorten

def test_shorten():
    assert shorten("hi how are you!")=="h hw r y!"
    assert shorten("hey come on be quick!")=="hy cm n b qck!"
    assert shorten("1234") == "1234"
    assert shorten("AExIOU") == "x"
