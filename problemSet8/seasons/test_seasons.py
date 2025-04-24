import pytest
from seasons import into_minutes

def test_into_minutes():
    dob = '20230111'
    assert into_minutes(dob) == 'One million, fifty-two thousand, six hundred forty minutes'

def test_invalid_date():

    assert into_minutes('20233501') == 'Invalid date'

    assert into_minutes('20233501') == 'Invalid date'

