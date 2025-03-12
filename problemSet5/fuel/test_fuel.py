import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("1/99") == 1
    assert convert("0/1") == 0

    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"

    with pytest.raises(ZeroDivisionError):
        assert convert("3/0")
    with pytest.raises(ValueError):
        assert convert("dog/cat")




