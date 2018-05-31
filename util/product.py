
from functools import reduce
from operator import mul

def product(iterable):
    return reduce(mul, iterable, 1)
