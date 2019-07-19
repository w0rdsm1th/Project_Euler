
"""
DIFFICULTY RATING: 5%
https://projecteuler.net/problem=57

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...


The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example
where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
"""
import functools
import itertools
import util

import matplotlib.pyplot as plt

"""LEARNINGS
- 'direction' to solve from, NOT solving from problem stated left to right (large to small terms)
but instead, from right to left. smallest term in the expansion 
computationally simpler? 

Also just follows the brackets!!

- simplify_fraction not needed?

"""


"""TODO 
- plot of the approximations approaching true 2**(-1/2) as n -> infinity

"""



"""
fractional addition



check for common 
"""


def UNDEEDED_simplify_fraction(numerator, denominator):
    num_factors = util.factors(numerator)
    denom_factors = util.factors(denominator)

    common_factors = set.intersection(num_factors, denom_factors)
    common_factors.remove(1)
    if common_factors:
        divisor = max(common_factors)
        # print(f"found common factor {divisor}")
        numerator, denominator = UNDEEDED_simplify_fraction(numerator / divisor, denominator / divisor)

    # print(f"done! returned {numerator} / {denominator}")
    return numerator, denominator


def incr_expansion(numerator, denominator, base=2):
    return denominator, (base * denominator + numerator)  # intentionally inverting


def add_constant(numerator, denominator, constant=1):
    return constant * denominator + numerator, denominator


def binom_expansion_gener(n, out_divide_tuple="tuple"):
    # calculating the fractional part
    numer = 1
    denom = 2
    for expan in range(n):
        if expan % 100 == 0:
            print(f"just passed {expan} loop")
            print(f"numerator: {numer}, denominator: {denom}")

        numer, denom = incr_expansion(numer, denom)

        # add the constant
        numer_const, denom_const = add_constant(numer, denom)

        if out_divide_tuple == "tuple":
            yield numer_const, denom_const

        elif out_divide_tuple == "divide":
            yield numer_const/denom_const


def len_check(int_1, int_2):
    return len(str(int_1)) > len(str(int_2))



# TODO PLOTTING the approach to the "true value" √ 2, 1.414...


# TEST CASES
UNDEEDED_simplify_fraction(577, 408)
UNDEEDED_simplify_fraction(239, 169)
UNDEEDED_simplify_fraction(99, 70)


if __name__ == '__main__':
    # n = 1_000
    # the_generator = binom_expansion_gener(n)
    # counter = sum([len_check(*next(the_generator)) for _ in range(n)])
    # print(f"answer: {counter}")

    n = 10
    the_generator_divide = binom_expansion_gener(n, "divide")
    actual_value_series = [2 ** .5, ] * n
    binom_expansion_series = [next(the_generator_divide) for _ in range(n)]

    plt.plot(range(n), binom_expansion_series, '', range(n), actual_value_series, 'r--')
    plt.show()



