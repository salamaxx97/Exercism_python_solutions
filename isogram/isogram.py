""" is it isogram ??? """
def is_isogram(word):
    """ is it isogram ??? """
    return not any(letter.isalpha() and word.lower().count(letter.lower()) > 1 for letter in word ) 