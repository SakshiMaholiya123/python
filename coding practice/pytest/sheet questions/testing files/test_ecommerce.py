import pytest
from ecommerce import calculate_total

def test_valid():
    items=[100,200,300]
    tax_rate=0.1
    res=calculate_total(items,tax_rate)
    assert res==660


def test_negative_price():
    items = [100,-50,200]
    tax_rate = 0.1

    with pytest.raises(ValueError, match="Item price cannot be negative"):
        calculate_total(items, tax_rate)


def test_invalid_tax():
    items=[100, 200]
    tax_rate=1.5   
    with pytest.raises(ValueError,match="Invalid tax rate"):
        calculate_total(items, tax_rate)