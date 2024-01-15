# The Geometrical position finder term of GP:
import math

def termOfGP(A, B, N):

    return math.floor(A * ((B / A) ** (N - 1)))

print(termOfGP(84, 87, 3))