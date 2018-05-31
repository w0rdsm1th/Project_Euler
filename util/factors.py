
from functools import reduce


def factors(n):
    """taken from: https://stackoverflow.com/a/6800214"""
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))

