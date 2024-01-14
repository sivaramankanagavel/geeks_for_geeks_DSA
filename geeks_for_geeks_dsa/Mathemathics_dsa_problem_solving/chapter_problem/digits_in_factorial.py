# Digits in factorial:
import math

def digits_in_factorial(number):

    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        digits = 0

        for i in range(2, number + 1):
            digits += math.log10(i)

        
        return math.floor(digits) + 1

print(digits_in_factorial(5))
print(digits_in_factorial(120))