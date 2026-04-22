""" CalculCalculate the number of grains of wheat on a chessboard.

 """
def square(index):
    """ the number of grains on a given square """
    if index < 1 or index > 64:
        raise ValueError("square must be between 1 and 64")
    return  2**(index-1)

def total():
    """the total number of grains on the chessboard"""
    summ=0
    for chess_square in range(1,65):
        summ += square(chess_square)
    return summ

print (square(1))
print (square(2))
print (square(3))