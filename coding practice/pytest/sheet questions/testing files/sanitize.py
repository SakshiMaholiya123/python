import re

class InputSanitizationError(Exception):
    pass

def sanitize_input(text):
    pattern=r"[^a-zA-Z0-9\s\-]"
    cleaned_text=re.sub(pattern, "",text)
    if not cleaned_text.strip():
        raise InputSanitizationError("sanitization resulted in empty text")
        
    return cleaned_text