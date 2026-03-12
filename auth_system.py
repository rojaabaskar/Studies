password = "45gsvghff"

def is_valid_length(password):
    return len(password) >= 8
print(is_valid_length(password))

def is_vaild_characters(password):
    
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_digit and has_upper

print(is_vaild_characters(password))
