""" different bases transformation """
def rebase(input_base, digits, output_base):
    """ different bases transformation """

    if input_base < 2 :
        raise ValueError("input base must be >= 2")
    if not all(0 <= digit < input_base for digit in digits):
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2 :
        raise ValueError("output base must be >= 2")

    base_10 = 0
    output = [] 
    for index,digit in enumerate(digits[::-1]):
        base_10+=digit*input_base**index
    
    if base_10 == 0 : return [0]

    while base_10 != 0 :
        output.append(base_10 % output_base)
        base_10 =int(base_10 / output_base)

    return output[::-1]


print(rebase(2, [1,0,0] , 10))