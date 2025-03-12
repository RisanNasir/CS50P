import pytest
import plates

def test_is_valid():
    assert plates.is_valid("AA") == True
    assert plates.is_valid("A2") == False
    assert plates.is_valid("2A") == False
    assert plates.is_valid("22") == False
    assert plates.is_valid(" 2") == False

    assert plates.is_valid("A") == False
    assert plates.is_valid("AAAAAAA") == False
    assert plates.is_valid("AA") == True
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("AAAAAA") == True


    assert plates.is_valid("11") == False
    assert plates.is_valid("50AA") == False
    assert plates.is_valid("8AAAAA") == False
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("CS5090") == True

    assert plates.is_valid("N1") == False
    assert plates.is_valid("1N") == False
    assert plates.is_valid("CS") == True
    assert plates.is_valid("61") == False
    assert plates.is_valid("6") == False


    assert plates.is_valid("CS50.") == False
    assert plates.is_valid(",N1N") == False
    assert plates.is_valid("CS??50") == False
    assert plates.is_valid("ABCDEF") == True


    assert plates.is_valid("00") == False
    assert plates.is_valid("CS05") == False
    assert plates.is_valid("0000") == False
    assert plates.is_valid("CS50") == True

    assert plates.is_valid("SA50A") == False
    assert plates.is_valid("SA500") == True
