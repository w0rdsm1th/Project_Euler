
import math
import operator as op
from functools import reduce

"""
https://projecteuler.net/problem=53

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =
n!
r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
"""

"""LEARNINGS
- timer using std lib itertools combinatorics versus own n_choose_r
- itertools reduce
"""


def own_factorial(n):
    # https://stackoverflow.com/a/4941932/3596968
    numerator = reduce(op.mul, range(1, n+1))
    denominator = ...
    return numerator // denominator


def n_choose_r(n, r):
    # return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
    # integer division "//" suggested in https://stackoverflow.com/a/4941846/3596968
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

n_choose_r(5, 3)

def q53(n_limit, threshold):
    n_start = 1
    over_threshold_combinations = []
    for n in range(n_start, n_limit+1):
        for r in range(1, n):
            if n_choose_r(n, r) > threshold:
                over_threshold_combinations.append((n, r))
    return over_threshold_combinations


if __name__ == '__main__':
    combos = q53(100, 1_000_000)
    print(len(combos))  # 4075

