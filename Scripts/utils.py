import string
import itertools

def generate_passwords(password_length, custom_charset="", with_custom_charset=False):
    """
    Generate all possible combinations of characters for a given length.
    """
    if with_custom_charset:
        all_combinations = itertools.product(custom_charset, repeat=password_length)
    else:
        all_combinations = itertools.product(string.printable, repeat=password_length)

    return ("".join(combination) for combination in all_combinations)
