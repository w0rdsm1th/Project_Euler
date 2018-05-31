
import util as ut
import math

"""
https://projecteuler.net/problem=51

Prime digit replacements

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

"""
# flexible index insert method
# e.g. with base number and indices to insert
# inputs: base_num [5, 6, 3], insert_indices [2, 3]



def replace_digits(base_list, insert_indices, replacement_digit):
    # insert_indices = sorted(insert_indices)
    output_list = base_list.copy()
    for idx in insert_indices:
        output_list.insert(idx, replacement_digit)

    return int(''.join(str(x) for x in output_list))

# ut.is_prime(replace_digits([5, 6, 3], [2, 3], 0))

def _internal_check(num_list, idxs):
    # if a first digit, cannot consider '0', e.g. 03 >> 3 and NOT part of the family
    list_replaced_digits = [replace_digits(num_list, idxs, same_int) for same_int in range(0, 10)]
    primes = [rep_dig for rep_dig in list_replaced_digits if ut.is_prime(rep_dig)]
    print(primes)
    return len(primes)

_internal_check([5, 6, 3], [2, 3])

# how to increment the search??
# start with list of primes, find those with 1 num diff

if __name__ == '__main__':
    pass
