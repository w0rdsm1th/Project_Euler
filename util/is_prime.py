
from math import ceil
import numba as nb


@nb.jit(nopython=True)
def is_prime(n):
    # early termination checks
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # else check for any divisors from 5 up to sqrt()+1, with stride 2
    else:
        for divisors in range(5, ceil(n**0.5)+1, 2):
            if n % divisors == 0:
                return False
        else:
            return True
