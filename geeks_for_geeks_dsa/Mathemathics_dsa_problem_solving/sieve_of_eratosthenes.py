# Sieve of eratosthenes means you may have to find the prime numbers upto the given number:
# this function time complexity is O(n * log(log(n))).

def sieve_of_eratosthenese(number):

    # inititalize the variable:
    p = 2

    # list comprehension for given the True value to all the numbers:
    prime = [True for i in range(number + 1)]

    # logic of the sieve here:
    while (p * p <= number):
        if prime[p] == True:
            for i in range(p * p, number + 1, p):
                prime[i] = False
        p += 1
    
    # print all prime numbers:
    for p in range(2, number + 1):
        if prime[p]:
            print(p, end=" ")

sieve_of_eratosthenese(15)
print(" ")
sieve_of_eratosthenese(20)
print(" ")
sieve_of_eratosthenese(10)
print(" ")
sieve_of_eratosthenese(30)
print(" ")