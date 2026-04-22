""" classify number """
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1 :
        raise ValueError("Classification is only possible for positive integers.")

    total = 0
    for count in range(1,number):
        if number % count == 0 :
            total += count 
    
    if number == total : return "perfect"
    if number > total : return "deficient"
    if number < total : return "abundant"
# print (classify(int(input())))