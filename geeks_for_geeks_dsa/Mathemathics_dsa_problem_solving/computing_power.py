# Find the power of the given number:

def computing_power(x, y):
    if x == 0:
        return 0
    elif y == 0:
        return 1
    else:
        # y is the power of the number when you doing the binary operation on this,
        # when ever the pit is set(1) we do the multiplication.

        res = 1

        while y > 0:

            # if the bit is set.
            if (y & 1) == 1:
                res = res * x
            
            x *= x
            y = y >> 1
        
        return res
    
print(computing_power(2, 5))