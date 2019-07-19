
"""
DIFFICULTY RATING: 20%
https://projecteuler.net/problem=60

The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
import functools
import itertools
import util

"""LEARNINGS
- 


n choose 5 

QQ how ensure that its "the lowest"?
"""


def check_prime_pair_set(prime_list):

    for idx, each_prime in enumerate(prime_list):
        for other_prime in prime_list[:idx] + prime_list[idx+1:]:
            composite_num = int(str(each_prime) + str(other_prime))
            # print(f"checking: {each_prime} and {other_prime}")
            if not util.is_prime(composite_num):
                print(f"returning False, problem nums: {each_prime} and {other_prime}")
                return False
    return True


def find_prime_pair_set(set_size, prime_list):
    while True:
        pass


find_prime_pair_set(4, None)


if __name__ == '__main__':
    check = check_prime_pair_set([3, 7, 109, 673])
    print(f"check status: {check}")



