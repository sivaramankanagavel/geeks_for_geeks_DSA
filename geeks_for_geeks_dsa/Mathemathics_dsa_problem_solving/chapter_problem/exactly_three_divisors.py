# Here you have to find out the exactly which numbers are divisible by only 3 numbers 1, self, <finded number>:
import math

def is_prime(num):
    if num <= 3:
        return True
            
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
        
    return True
            
                
def exactly3Divisors(N):
    # code here
    result = 0
                
    for num in range(2, int(math.sqrt(N)) + 1):
        if is_prime(num) and num * num <= N:
            result += 1
        
    return result

print(exactly3Divisors(30))
print(exactly3Divisors(10))
        