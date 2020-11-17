import string


def len_enough(code):
    """Vin Code should be exactly 17 characters"""
    return len(code) == 17


def has_lowercase(code):
    """Vin Code shouldn't contain a lowercase letters"""
    return len(set(string.ascii_lowercase).intersection(code)) > 0


def has_uppercase(code):
    """Vin Code must contain an uppercase letters"""
    return len(set(string.ascii_uppercase).intersection(code)) > 0


def has_numeric(pw):
    """Vin Code must contain a digits"""
    return len(set(string.digits).intersection(pw)) > 0
