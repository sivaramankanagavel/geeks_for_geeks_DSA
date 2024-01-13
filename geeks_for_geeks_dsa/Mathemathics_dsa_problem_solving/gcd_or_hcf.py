# GCD (Greatest Common Divisor) or HCF (Highest Common Factor):

def gcd_or_hcf(x, y):
    if x % y == 0:
        return y
    return gcd_or_hcf(y, x % y)

print(gcd_or_hcf(60, 48))
print(gcd_or_hcf(98, 56))