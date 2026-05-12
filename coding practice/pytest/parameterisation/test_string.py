import pytest

def isadmin(role):
    return role.lower()=="admin"

@pytest.mark.parametrize("role,expected",[
    ("admin", True),
    ("ADMIN", True),
    ("guest", False),
    ("editor", False),
    ("", False)
])

def test_isadmin(role,expected):
    assert isadmin(role)==expected
    