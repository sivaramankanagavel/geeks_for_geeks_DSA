# Print all the prime factors for the given number:
import math

def prime_factors(number):

    # if even number comes we run this loop untill the number becomes odd.
    while number % 2 == 0:
        print(2)
        number = number / 2
    
    # once number becomes odd we run this loop untill the number becomes 1.
        # we run this loop upto the sqrt(number) because that square-root of the number is always becomes 
        # itself to the number.
    for i in range(3, int(math.sqrt(number)) + 1, 2):

        while number % i == 0:
            print(i)
            number = number / i

    # this is used to print the prime numbers invoived in this calculation.
    if number > 2:
        print(int(number))

print(prime_factors(315))
print(prime_factors(15))