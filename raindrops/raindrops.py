""" ringing pills"""
def convert(number):
    """ checking number ring """
    ring=""
    if  number % 3==0 :
        ring+= "Pling" 
    if number % 5==0 :
        ring+= "Plang"
    if number % 7==0: 
        ring+= "Plong"
    return ring if ring else str(number)
