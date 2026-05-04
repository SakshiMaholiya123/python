import pytest
from employee import validate_employee
def test_validate_employee_success():
    assert validate_employee("EMP-1234", "jane.doe@company.com") is True

def test_validate_employee_invalid_id():
    with pytest.raises(ValueError, match="Invalid Employee ID format"):
        validate_employee("EMP-12", "jane.doe@company.com")

def test_validate_employee_invalid_email():
    with pytest.raises(ValueError, match="Invalid Email format"):
        validate_employee("EMP-1234", "john@gmail.com")