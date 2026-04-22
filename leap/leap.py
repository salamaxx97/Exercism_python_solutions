""" is the year a leap year """
def leap_year(year):
    """ is the year a leap year """
    if year % 4 !=0 :
        return False
    if year % 100 == 0 and not year % 400 ==0 :
        return False 
    return True 
print (leap_year(1997))
print (leap_year(1900))
print (leap_year(2024))