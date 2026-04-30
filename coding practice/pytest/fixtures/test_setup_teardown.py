import pytest

@pytest.fixture
def database_connection():
    db={"status":"connected","data":[]}
    print("database connection start")
    yield db
    db["status"]="closed"
    print("database connection ends")


def test_connection(database_connection):
    database_connection["data"].append("rec_1")
    assert "rec_1" in database_connection["data"]
    assert database_connection["status"]=="connected"