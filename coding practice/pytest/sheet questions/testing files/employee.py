import re

def validate_employee(emp_id, email):
    id_pattern = r"^EMP-\d{4}$"
    email_pattern = r"^[a-zA-Z0-9._%+-]+@company\.com$"

    if not re.match(id_pattern, emp_id):
        raise ValueError(f"Invalid Employee ID format{ emp_id}")

    if not re.match(email_pattern, email):
        raise ValueError(f"Invalid email format{email}")

    return True