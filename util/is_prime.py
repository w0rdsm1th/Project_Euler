
from math import ceil


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    else:
        if any(n%divisors == 0 or n%(divisors+2) == 0 for divisors in range(5, ceil(n**0.5)+1, 2)):
            return False
        else:
            return True
