# All divisors of the number:
import math

def all_divisors(number):

    i = 1

    while i <= math.sqrt(number):
        if number % i == 0:
            # if the (n / i) as well as the i is equal then print i only. else print i along with (n/i).
            if (number / i == i):
                print(i, end=" ")
            else:
                print(i, int(number/ i), end=" ")
        
        i += 1

all_divisors(10)
print("\n")
all_divisors(20)