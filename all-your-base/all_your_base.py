""" different bases transformation """
def rebase(input_base, digits, output_base):
    """ different bases transformation """

    if input_base < 2 :
        raise ValueError("input base must be >= 2")
    if not any(0 <= int(digit) < input_base for digit in str(digits)):
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2 :
        raise ValueError("output base must be >= 2")

    base_10 = 0
    temp = digits  
    output = 0 
    index = 0
    while digits != 0 :
        base_10+=digits % 10 * input_base ** index
        digits = int(digits/10) 
        index += 1
    return base_10

print(rebase(2, 10001, 10))