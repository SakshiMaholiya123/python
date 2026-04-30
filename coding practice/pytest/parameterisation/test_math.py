import pytest

def add(num1,num2):
    return num1+num2

@pytest.mark.parametrize("num1,num2,expected",[
    (2, 3, 5),     
    (10, 20, 30),   
    (0, 0, 0),      
    (-1, 1, 0)
])

def test_add(num1,num2,expected):
    assert add(num1,num2)==expected
