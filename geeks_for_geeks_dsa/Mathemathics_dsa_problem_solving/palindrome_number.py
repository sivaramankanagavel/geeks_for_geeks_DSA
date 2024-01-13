# Find the palindrome of the given number:

def palindrome_number(N):
    reverse = 0
    temp = N

    while temp > 0:
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10
    
    if reverse == N:
        return True
    
    return False

print(palindrome_number(1221))
print(palindrome_number(2332))
print(palindrome_number(2341))