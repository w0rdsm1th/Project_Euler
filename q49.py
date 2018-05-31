
import util as ut
import math

"""
https://projecteuler.net/problem=49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""


# 1 other 4 digit increasing sequence
# find primes, that are  permutations
def is_permutation(base, to_check):
    # if nums not equal and contain all same numbers then are permutations of each other
    if int(base) != int(to_check) and sorted(str(base)) == sorted(str(to_check)):
        return True
    return False

def find_same_abs(primes):
    for each_prime in primes:
        diffs = [abs(n - each_prime) for n in primes]
        if len(set(diffs)) != len(diffs):
            print('found candidate: {0}!'.format(each_prime))
            duplicates = [pr for pr in diffs if diffs.count(pr) == 2]
            repeated_diff_indices = [i for i, x in enumerate(diffs) if x == duplicates[0]]
            filtered_primes = [primes[i] for i, pr in enumerate(primes) if i in repeated_diff_indices]

            return [each_prime, ] + filtered_primes

    return False


if __name__ == '__main__':
    # test cases
    # assert is_permutation(1487, 4817)
    # assert is_permutation(1487, 8147)

    # approaches
    # 1
    # list primes in 1000 to 9999, find permutations

    # 2
    # for each prime in sequence, check if any permutations also prime

    # approach 1
    primes = [n for n in range(999, 10000) if ut.is_prime(n)]
    for each_prime in primes:
        prime_permuts = [n for n in primes if is_permutation(each_prime, n)]
        same_abs = find_same_abs(prime_permuts)

        if same_abs and same_abs[0] != 4817:
            print(same_abs)
            # 296962999629
