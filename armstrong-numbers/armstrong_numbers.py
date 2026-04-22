"""Caculate to see if number is armstrong """
def is_armstrong_number(number):
    """Caculate to see if number is armstrong """

    armstrong = 0
    str_num=str(number)
    
    for digit in str_num :
        armstrong += int(digit) ** len(str_num) 
    if armstrong == number :
        return True
    return False 

print (is_armstrong_number(153))