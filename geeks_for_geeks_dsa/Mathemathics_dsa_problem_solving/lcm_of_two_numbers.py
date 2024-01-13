# LCM of two numbers:
# we used the a * b = lcm(a, b) * gcd(a, b)

from gcd_or_hcf import gcd_or_hcf

def lcm_of_two_numbers(x, y):
    
    gcd_value = gcd_or_hcf(x, y)

    return int((x * y) / gcd_value)

print(lcm_of_two_numbers(20, 15))