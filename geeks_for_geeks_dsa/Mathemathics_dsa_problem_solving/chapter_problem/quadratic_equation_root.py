# Quadratic Equation Root:
import math

def quadratic_equation_root(a, b, c):
    
    # This imaginary part should be equal or greather than zero 
    # (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a). --> # Real and distinct roots.
    # if it's negative then we return -1.
    # exactly zero also we return -b / (2 * a). --> # Real and equal roots.

    imaginary_part = (b ** 2) - (4 * a * c)
    divider = 2 * a

    if imaginary_part > 0:
        root1 = (-(b) + math.sqrt(imaginary_part)) / divider
        root2 = (-(b) - math.sqrt(imaginary_part)) / divider

        if root1 > root2:
            return [math.floor(root1), math.floor(root2)]
        else:
            return [math.floor(root2), math.floor(root1)]
    
    elif imaginary_part == 0:
        root = -b / divider
        return[math.floor(root), math.floor(root)]
    
    else:
        return [-1]
    