""" crypto using rotcipher""" 

from string import ascii_lowercase,ascii_uppercase
def rotate(text, key):
    """ crypto usin grotcipher""" 
    key = key % 26
    lower_alpha = ascii_lowercase
    upper_alpha = ascii_uppercase
    alphapet=upper_alpha+lower_alpha

    shifted_lower=lower_alpha[key:]+lower_alpha[:key]
    shifted_upper=upper_alpha[key:]+upper_alpha[:key]
    shifted = shifted_upper+shifted_lower
    table = str.maketrans(alphapet,shifted)

    return text.translate(table)

    