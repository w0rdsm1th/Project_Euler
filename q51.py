
import math
import itertools as it
import numpy as np

import util as ut


"""
https://projecteuler.net/problem=51

Prime digit replacements

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, 
this 5-digit number is the first example having seven primes among the ten 
generated numbers, yielding the family: 
56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number 
(not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

"""
# flexible index insert method
# e.g. with base number and indices to insert
# inputs: base_num [5, 6, 3], insert_indices [2, 3]

"""LESSONS LEARNED
- insert default behaviour
- "in" prime_list 
- early exit if not prime
- insert default behaviour if index is longer than list
t = [1, 2]
t.insert(5, 6)

"""

# 113 and 173 are prime
# check_prime_family([1, 3], [0], 3)
# check_prime_family([1, 3], [1], 3)
# check_prime_family([1, 3], [2], 6)
#
# check_prime_family([3], [0], 5)
# check_prime_family([3], [1], 9)
# check_prime_family([5, 6, 3], [2, 3], 7)
#
# # example of 19, 29
# check_prime_family([9], [0])
# check_prime_family([9], [1])
# check_prime_family([9], [2])


def q51_first_attempt(threshold_prime_family_len):
    """
    goal: performing smallest possible increase in val, by incrementing the IDX

    in order, return all possible combinations of replacement up to whole number
    e.g.
    outer loop: controls the fixed_idxs
    [00000]
    ...
    [000*1]
    [000*2]  - not worth considering even numbers
    [000*3]
    ... skeleton [1, ]
    [0001*] - won't achieve, max 5 odd numbers
    [0002*]
    [0002*]
    ...
    [0010*] - won't achieve, max 5 odd numbers
    [001*1]
    [001*3]
    [001*5]
    ...
    [002*1]
    [002*3]
    [002*5]
    ...
    [009*9]
    [00**9] - all smaller than above? and covered previously
    [010*1]


    inner loop: controls the rotating_idxs
    [5600*] - won't achieve, max 5 odd numbers
    [560*1]
    [560*3]
    [560*5]
    [560**] - not worth considering even numbers
    [56*0*]
    [56**3]
    [56***]  set-dff those already checked? and smaller numbers?
    [5*003]
    [5*00*]
    [5*0**]
    [5****] # reached threshold, need an IDX rollover
    [*6003] #    rollover
    [*600*]
    [*60*3]
    [*60**]
    [56**3]

    move along OR increase number of replacements

    then increase number of wildcards? and increment?

    :param base_num int:
    :return:
    """
    skeleton = [1]
    srch_idxs = [0]
    while True:
        prime_family = check_prime_family(skeleton, srch_idxs)
        if len(prime_family) >= threshold_prime_family_len:
            print("found!: ", prime_family)
            return prime_family

        # considered all srch_idxs combinations possible, increment the skeleton
        if srch_idxs[0] == 0 and len(srch_idxs) == len(skeleton):
            # addition to base
            if skeleton[0] != 9:
                skeleton[1:] += 2  # stride of 2: only worth considering odd numbers
            # rollover skeleton and reset srch_idxs
            else:
                skeleton = [1] + [0]*len(skeleton)
                srch_idxs = [len(skeleton)]

        # increment the srch_idxs: from right hand side, shift up one. and reset the next idx along
        else:
            # case where srch_idxs are exactly ascending
            if srch_idxs == range():
                pass



# Q: how to increment the search??
# 1) combinations of indexes and base nums
# searching over list of primes, increment primes in batches
# batch_size = 100
# base_num = 3  # starting at smallest odd prime because striding by 2
# stopping_family_length = 7
# idxs = [0]
# seen_primes = set()

# while True:
#     prime_batch = set(val for val in range(base_num, base_num+batch_size, 2) if ut.is_prime(val))
#     prime_batch = list(prime_batch - set(seen_primes))
#     seen_primes.update(prime_batch)
#
#     for prime in prime_batch:
#         idxs = idx_combinations(base_num)
#
#         for idx in idxs:
#
#             list_prime = list(str(prime))
#
#             prime_family = check_prime_family(list_prime, idx)
#             if len(prime_family) == stopping_family_length:
#                 print("found! family: {0}".format(prime_family))
#                 break




# 2) start with list of primes, find those with 1 num diff? increase search to 2 diff
t = [56003, 56113, 56333, 56443, 56663, 56773, 56993]
# differences will always be same (1x) OR double (2x):
# 56113 - 56003 = 110
# 56443 - 56333 = 110
# BUT unknown number of primes between them, so need to take difference combinations of all primes


# 3) NEW IDEA: combination of difference between combinations,
# and converting all to string, sort the individual strings and find by stride??
# doesnt work, not adjacent
# sorting by minimal replacements??
# primes = sorted([str(num) for num in range(56000, 57000) if ut.is_prime(num)])
# chunking search by those primes that are the same length??
# IF nums are 1, 2 transformations away

def n_replacement_away(num1, num2, n_trans):
    li_num1, li_num2 = list(str(num1)), list(str(num2))

    diff = [idx_num1 for (idx_num1, val_num1), val_num2 in zip(enumerate(li_num1), li_num2) if val_num1 != val_num2]

    if len(li_num1) != len(li_num2) or len(diff) != n_trans:
        return False, []

    else:
        return True, diff


###################################################################
# 4) iterating over list of known primes

class q51:
    def __init__(self, family_len, inp_primes):
        self.family_len = family_len
        self.complement_not_prime_len = 10 - family_len

        self.inp_primes = inp_primes

    @staticmethod
    def powerset(iterable):
        """
        powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
        from https://docs.python.org/3/library/itertools.html
        """
        return it.chain.from_iterable(it.combinations(iterable, r) for r in range(1, len(iterable)+1))

    def check_prime_family(self, num_list, idxs):

        non_prime_family_count = 0
        out_primes = []

        def _replace_digits(base_list, insert_indices, replacement_digit):
            for idx in insert_indices:
                # if a first digit, cannot consider '0', e.g. "03" >> 3 and NOT part of the family
                if idx == 0 and replacement_digit == 0:
                    return None
                base_list = base_list[:idx] + [replacement_digit] + base_list[idx:]

            out = int(''.join(str(x) for x in base_list))
            return out

        # apply replacement digits for indices for 0 to 9
        list_replaced_digits = [_replace_digits(num_list, idxs, replacement_int) for replacement_int in range(0, 10)]

        for rep_dig in list_replaced_digits:
            # early exit
            if non_prime_family_count >= self.complement_not_prime_len:
                return False
            # increment non-prime, to approach early exit
            if rep_dig not in prime_list:
                non_prime_family_count += 1
            else:
                out_primes.append(rep_dig)

        print(f"Found! Length prime family: {len(out_primes)}")
        print(out_primes)
        return out_primes

    def find_indices_to_replace(self, inp_num) -> list:

        # cannot consider rightmost because seeking 8 len prime family, rightmost would yield 5 even numbers
        # right to left, return index lower or equal to 2.
        # in order to achieve prime family len of 8, prime family replacement digits needed of 2 or less
        replace_idxs = [idx for idx, val in enumerate(inp_num[:-1]) if val <= self.complement_not_prime_len][::-1]

        # indices to replace depend on the length of inp_num
        # consider the smallest increment combinations of the indices
        # e.g. [3, 2], [3, 1]
        if not replace_idxs:
            return []
        if len(replace_idxs) == 1:
            return [replace_idxs]
        if len(replace_idxs) > 1:
            return self.powerset(replace_idxs)

    def preprocess_prime_list(self, inp_primes, start_idx=5):
        """
        generator to filter for "valid" primes
        :param inp_primes:
        :param start_idx: skip the single digit primes, not worth considering
        :return:
        """
        for each_prime in inp_primes[start_idx:]:
            listified = [int(_) for _ in list(str(each_prime))]
            indices = self.find_indices_to_replace(listified)
            if indices:
                yield indices, listified

    @ut.timer
    def solve(self):
        search_primes = self.preprocess_prime_list(prime_list)
        for replace_idxs, candidate in search_primes:
            for each_idx in replace_idxs:

                # filter the replacement index out of the candidate number
                iter_list = [val for idx, val in enumerate(candidate) if idx not in each_idx]

                if iter_list:
                    check = self.check_prime_family(iter_list, each_idx)

                    if check:
                        return check


if __name__ == '__main__':

    prime_finder = ut.PrimeFinder("util/primes.pickle")
    prime_list = prime_finder.read_prime_pickle()

    solver = q51(7, prime_list)
    solver.solve()


# def index_combinations(inp_idxs):
#     # adapted from https://chrisalbon.com/python/basics/all_combinations_of_a_list_of_objects/
#     # Finds every combination(without replacement) for each object in the list
#     combinations = []
#     for i in range(len(inp_idxs)):
#         combinations.extend(list(it.combinations(inp_idxs, i+1)))
#
#     # Flatten the list of iterators into a single list
#     # combinations = [row for row in combinations]
#     # combinations = [_ for row in combinations for _ in row]
#     return combinations
