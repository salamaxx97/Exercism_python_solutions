""" define score of dar in circle with 10 units radius """
def score(x, y):
    """ - If the dart lands outside the target, player earns no points (0 points).
- If the dart lands in the outer circle of the target, player earns 1 point.
- If the dart lands in the middle circle of the target, player earns 5 points.
- If the dart lands in the inner circle of the target, player earns 10 points.

The outer circle has a radius of 10 units (this is equivalent to the
total radius for the entire target), the middle circle a radius of 5 units, and the inner
circle a radius of 1."""
    if x**2 + y **2 <= 1 : 
        return 10
    if x**2 + y **2 <= 25 : 
        return 5 
    if x**2 + y **2 <= 100 : 
        return 1 
    return 0 