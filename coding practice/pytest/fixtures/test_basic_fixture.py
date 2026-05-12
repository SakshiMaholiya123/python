import pytest

@pytest.fixture
def user():
    return {"username":"Sakshi","access_level":"admin"}

def test_user_permission(user):
    assert user["username"]=="Sakshi"
    assert user["access_level"]=="admin"
    #assert user["username"]=="sakshi"  # giving error as "sakshi and Sakshi are different"
    

   
