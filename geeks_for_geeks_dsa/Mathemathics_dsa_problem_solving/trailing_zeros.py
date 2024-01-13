# Trailing of zero's:
# 1. the trailing of zero's was calculated based on the factorial of the given number. 
# 2. the zero's was started from 5! only before that we didn't have the factorial.
# the time complexity O(log5n)

def trailing_of_zeros(N):
    count = 0
    i = 5

    while N / i >= 1:
        count += int(N / i)
        i *= 5
    
    return int(count)

print(trailing_of_zeros(100))
print(trailing_of_zeros(8))