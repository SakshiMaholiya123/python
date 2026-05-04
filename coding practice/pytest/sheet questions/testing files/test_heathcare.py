import pytest
from healthcare import validate_patient,PatientValidationError 

def test_validate_patient_success():
    assert validate_patient(30, 72) is True
    assert validate_patient(0, 20) is True  
    assert validate_patient(120, 220) is True  

def test_validate_patient_invalid_age():
    with pytest.raises(PatientValidationError, match="invalid age: 150"):
        validate_patient(150, 80)

def test_validate_patient_invalid_heart_rate():
    with pytest.raises(PatientValidationError, match="invalid heart rate: 10"):
        validate_patient(45, 10)