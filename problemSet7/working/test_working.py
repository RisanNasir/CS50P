import pytest
from CodeProjects.Python.problemSet7.working.working import convert

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_omit_to():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
        convert("10:7 AM - 5:1 PM")
def test_outofrange():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")
