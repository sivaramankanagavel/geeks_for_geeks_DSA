# find the count of digits on given number:

def count_of_digits(N):
    i = 0

    while N > 0:
        N = N // 10
        i += 1
    
    return i

print(count_of_digits(2334))