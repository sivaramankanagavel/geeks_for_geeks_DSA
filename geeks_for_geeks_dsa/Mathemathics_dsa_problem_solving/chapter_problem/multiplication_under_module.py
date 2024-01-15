# Multiplication under module:
# (10 ** 9 + 7) this value was given in the Question directly we take from that.

def multiplication_under_module(a, b):

    return (a * b) % (10 ** 9 + 7)

a = 92233720368547758
b = 92233720368547758
print(multiplication_under_module(a, b))