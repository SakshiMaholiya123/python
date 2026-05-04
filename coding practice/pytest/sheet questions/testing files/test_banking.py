
import pytest
from banking import transfer,TransferError
def test_transfer_success():
    assert transfer("1234567890", "0987654321", 100, 500) is True

def test_transfer_zero_amount():
    with pytest.raises(TransferError):
        transfer("1234567890", "0987654321", 0, 500)

def test_transfer_insufficient_balance():
    with pytest.raises(TransferError):
        transfer("1234567890", "0987654321", 1000, 500)

def test_transfer_invalid_account():
    with pytest.raises(TransferError):
        transfer("12345", "0987654321", 100, 500)