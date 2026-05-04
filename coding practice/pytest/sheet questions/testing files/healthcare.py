
class PatientValidationError(Exception):
    pass

def validate_patient(age, heart_rate):
    if not (0 <= age <= 120):
        raise PatientValidationError(f"invalid age {age} must be between 0 and 120.")
    if not (20 <= heart_rate <= 220):
        raise PatientValidationError(f"invalid heart rate {heart_rate} must be between 20 and 220.")
    
    return True