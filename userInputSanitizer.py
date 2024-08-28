def is_int(s):
    try:
        int(s)  # Tente de convertir en entier
        return True
    except ValueError:
        return False
    
def is_non_negative_integer(value):
    if is_int(value):
        return int(value) > 0
    return False

def is_valid_string(s):
    return bool(s.strip())