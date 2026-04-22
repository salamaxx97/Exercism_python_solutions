"""Determine if a triangle is equilateral, isosceles, or scalene.

"""
def is_triangle(sides):
    """Determine if it is  a triangle 
"""
    sides=sorted(sides)
    return sum(sides[0:2])>=sides[2] and sides[0] !=0

def equilateral(sides):
    """An equilateral triangle has all three sides the same length.

""" 
    return is_triangle(sides) and len(set(sides)) == 1 



def isosceles(sides):
    """An isosceles triangle has at least two sides the same length. """
    return is_triangle(sides) and len(set(sides)) <= 2


def scalene(sides):
    """A scalene triangle has all sides of different lengths.

"""
    return is_triangle(sides) and len(set(sides)) == 3