
import pytest
from sanitize import sanitize_input,InputSanitizationError
def test_sanitize_name_with_special():
    assert sanitize_input("John Doe!")=="John Doe"

def test_sanitize_empty_result():
    with pytest.raises(InputSanitizationError, match="empty text"):
        sanitize_input("!@#$%")

def test_sanitize_payment_string():
    assert sanitize_input("Payment 100$")=="Payment 100"