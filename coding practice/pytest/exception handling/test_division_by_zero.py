import pytest

# def test_division_by_zero():
#     with pytest.raises(ZeroDivisionError):
#         190/0

#to add the or to check for the multiple tast cases ,hee we can use the parameterised marker

@pytest.mark.parametrize("num, deno", [
    (10, 2), 
    (5, 0), 
    (20, 5),
    (20,0)
])
def test_logic(num,deno):
    if deno==0:
        with pytest.raises(ZeroDivisionError):
            res=num/deno

    else:
        assert num/deno==(num/deno)