# Modular Multiplicative Inverse:

# Input:
# a = 3
# m = 11
# Output: 4
# Explanation: Since (4*3) mod 11 = 1, 4 
# is modulo inverse of 3. One might think,
# 15 also as a valid output as "(15*3)
# mod 11"  is also 1, but 15 is not in 
# ring {0, 1, 2, ... 10}, so not valid.

def modInverse(a,m):
    ##Your code here
        
    i = 1
        
    while i <= m:
        if ((i * a) % m == 1):
            return i
        else:
            i += 1
            continue
        
    return -1

print(modInverse(3, 11))
print(modInverse(10, 17))