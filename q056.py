
"""
DIFFICULTY RATING: 5
https://projecteuler.net/problem=56

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""
import functools
import itertools
import util
from numba import jit
import time

"""LEARNINGS
"""


def sum_digits_loop(inp):
    total = 0
    for digit in str(inp):
        total += int(digit)
    return total


def sum_digits_list_comp(inp):
    inp_digits_list = [int(dig) for dig in list(str(inp))]
    return sum(inp_digits_list)


# @jit()
@jit(nopython=True)  # doesnt work for Python string types, mainly only numpy types
def sum_digits_numba(inp):
    total = 0
    for digit in inp:
        total += int(digit)
    return total

@jit(nopython=True)  # doesnt work for Python types, mainly only numpy types
def sum_digits_numba_numpy(inp):
    pass


def q56_solver(a_min=1, a_max=100, b_min=1, b_max=100, solver=sum_digits_list_comp):
    all_powers = [str(a**b) for a in range(a_min, a_max) for b in range(b_min, b_max)]
    sum_digits_all_powers = list(map(solver, all_powers))
    return max(sum_digits_all_powers)


if __name__ == '__main__':

    start = time.time()
    print("baseline sum: ", q56_solver(a_min=12, b_min=2, solver=sum_digits_loop))
    end = time.time()
    print("baseline elapsed = %s" % (end - start))

    # compiling with numba first for limited range
    start = time.time()
    print("numba limited run sum: ", q56_solver(a_min=1, a_max=3, b_min=1, b_max=3, solver=sum_digits_numba))
    end = time.time()
    print("Numba elapsed (with compilation) = %s" % (end - start))

    # NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE
    start = time.time()
    print("numba digital sum: ", q56_solver(a_min=12, b_min=2, solver=sum_digits_numba))
    end = time.time()
    print("Numba elapsed (after compilation) = %s" % (end - start))




