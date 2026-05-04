import pytest

def cal_age(birth_year):
    if birth_year<0:
        raise ValueError("year cannot be -ve")
    return 2026-birth_year

def test_message():
    with pytest.raises(ValueError,match="year cannot be -ve"):
        cal_age(-10)   