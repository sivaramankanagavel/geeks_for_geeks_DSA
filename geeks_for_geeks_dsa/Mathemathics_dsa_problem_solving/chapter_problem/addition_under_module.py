# Addition Under Module:
import math

def addition_under_module(a, b):

    return (a + b) % (10 ** 9 + 7)

a = 9223372036854775807
b = 9223372036854775807
print(addition_under_module(a, b))