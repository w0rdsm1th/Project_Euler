
import util as ut
import math
from copy import deepcopy

"""
https://projecteuler.net/problem=50

Consecutive prime sum
Problem 50 
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""
# approaches
# for each prime, try and find if can be written as consecutive sum
# for consecutive series of primes, find if sum is prime


# ambiguities:
# - if can double up in the sequence
# - if 'starting' point always 2 >> doubt it, want a way of generating sliding window on list of primes


def prime_genr(n=1):
    while True:
        if ut.is_prime(n):
            yield n
        n += 1

prime_generator = prime_genr()
next(prime_generator)


def prime_list(lb=1, ub=100):
    return [n for n in range(lb, ub) if ut.is_prime(n)]


# tests cases
# 41
# 953

def check_consecutive_sums(up_limit):
    # start at 2,... check if hits or goes over
    # then increment to 3, ...
    primes = prime_list(1, up_limit)
    max_len_seq = []

    for each_prime in primes[::-1]:
        start_idx, end_idx = 0, 1
        max_end_idx = primes.index(each_prime)

        # progress report print
        if each_prime % 100_000 == 0:
            print("current prime {0}".format(each_prime))

        # inner loop, checking if/how prime can be written as consecutive seq
        while start_idx < len(primes) and end_idx < max_end_idx:
            curr_slice = primes[start_idx:end_idx]

            if sum(curr_slice) == each_prime:
                # print('found! {0}, len consecutive {1}'.format(each_prime, len(curr_slice)))
                # print('sequence: {0}'.format(curr_slice))
                if len(curr_slice) > len(max_len_seq):
                    max_len_seq = deepcopy(curr_slice)
                    print("new max len sequence found, num {0}, len seq {1}, {2}".format(each_prime,
                                                                                         len(max_len_seq),
                                                                                         max_len_seq,
                                                                                         ))
                break

            elif sum(curr_slice) < each_prime:
                end_idx += 1

            elif sum(curr_slice) > each_prime:
                start_idx += 1
                end_idx = start_idx + 1


if __name__ == '__main__':
    # check_consecutive_sums(43)
    # check_consecutive_sums(954)
    check_consecutive_sums(1_000_000)
    # 997_651


