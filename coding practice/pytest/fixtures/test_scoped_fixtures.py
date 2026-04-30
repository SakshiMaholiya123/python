import pytest

@pytest.fixture
def api_token():
    print("fetching api token")
    return "token_123"

def test_api_token_a(api_token):
    assert api_token=="token_123"

def test_api_token_b(api_token):
    assert api_token.startswith("token")