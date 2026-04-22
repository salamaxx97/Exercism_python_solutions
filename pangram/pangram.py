"""check if sentence has all alphapet letters """
def is_pangram(sentence):
    """check if sentence has all alphapet letters """
    new_sentence=[]
    for letter in sentence :
        if letter.isalpha() :
            new_sentence.append(letter.lower())
    return len(set(new_sentence)) == 26 