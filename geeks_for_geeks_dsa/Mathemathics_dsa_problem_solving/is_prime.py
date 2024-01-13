# to find the number is prime or not:
# why we used the while loop here for the reason of when we checking the prime number less than < 1to 25 
# is find out from the remaing condition but above 25 to n numbers is count on the while loop. 

def is_prime(number):
    if number == 0:
        return False
    elif number == 2 or number == 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    
    i = 5

    while i * i < number:
        if number % i == 0 or number % (i + 2):
            return False
        i += 6
    
    return True

print(is_prime(6))
print(is_prime(21))
print(is_prime(34))
print(is_prime(5))
print(is_prime(11))