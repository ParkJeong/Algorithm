import sys
import math


def binomial_coefficient(n, k):
    factorial = math.factorial
    return factorial(n) // (factorial(n-k) * factorial(k))


n, k = map(int, sys.stdin.readline().rstrip().split())
# print(binomial_coefficient(n, k))
print(math.comb(n, k))