import pytest

# define out own markers to run the group test  into categories like smoke ,regresssion
@pytest.mark.smoke    # it is smoke marker
def test_print_statement():
    print("statement print")
    assert True

def test_fun():   # not marked as smoke and it is a regular test
    print("function executes")
    assert True


@pytest.mark.regression
def test_reg():
    print("regression test")
    assert True