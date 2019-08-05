
import util as ut
import math


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
- 
"""

def check_prime_family(num_list, idxs):

    def _replace_digits(base_list, insert_indices, replacement_digit):
        # no need to sort inputs, we control the increment of indices
        # insert_indices = sorted(insert_indices)
        output_list = base_list.copy()
        for idx in insert_indices:
            output_list.insert(idx, replacement_digit)

        out = int(''.join(str(x) for x in output_list))
        # if a first digit, cannot consider '0', e.g. "03" >> 3 and NOT part of the family
        if len(str(out)) != len(output_list):
            return None
        return out

    list_replaced_digits = [_replace_digits(num_list, idxs, replacement_int) for replacement_int in range(0, 10)]
    primes = [rep_dig for rep_dig in list_replaced_digits if rep_dig and ut.is_prime(rep_dig)]

    return primes

# insert default behaviour if index is longer than list
t = [1, 2]
t.insert(5, 2)


# 113 and 173 are prime
check_prime_family([1, 3], [0])
check_prime_family([1, 3], [1])
check_prime_family([1, 3], [2])

check_prime_family([3], [0])
check_prime_family([3], [1])
check_prime_family([5, 6, 3], [2, 3])
len(check_prime_family([5, 6, 3], [2, 3]))
# example of 19, 29
check_prime_family([9], [0])
check_prime_family([9], [1])
check_prime_family([9], [2])

def q51(threshold_prime_family_len):
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


if __name__ == '__main__':
    test_run = q51(7)
    print(test_run[0])
    actual_run = q51(7)


# Q: how to increment the search??
# 1) combinations of indexes and base nums
# searching over list of primes, increment primes in batches
batch_size = 100
base_num = 3  # starting at smallest odd prime because striding by 2
stopping_family_length = 7
idxs = [0]
seen_primes = set()

while True:
    prime_batch = set(val for val in range(base_num, base_num+batch_size, 2) if ut.is_prime(val))
    prime_batch = list(prime_batch - set(seen_primes))
    seen_primes.update(prime_batch)

    for prime in prime_batch:
        idxs = idx_combinations(base_num)

        for idx in idxs:

            list_prime = list(str(prime))

            prime_family = check_prime_family(list_prime, idx)
            if len(prime_family) == stopping_family_length:
                print("found! family: {0}".format(prime_family))
                break




# 2) start with list of primes, find those with 1 num diff? increase search to 2 diff
t = [56003, 56113, 56333, 56443, 56663, 56773, 56993]
# differences will always be same (1x) OR double (2x):
# 56113 - 56003 = 110
# 56443 - 56333 = 110
# BUT unknown number of primes between them, so need to take difference combinations of all primes


# 3) NEW IDEA: convert all to string, sort and find by stride??
# doesnt work, not adjacent
# sorting by minimal replacements??
primes = sorted([str(num) for num in range(56000, 57000) if ut.is_prime(num)])
# chunking search by those primes that are the same length??
# IF nums are 1, 2 transformations away

def n_replacement_away(num1, num2, n_trans):
    li_num1, li_num2 = list(str(num1)), list(str(num2))

    diff = [idx_num1 for (idx_num1, val_num1), val_num2 in zip(enumerate(li_num1), li_num2) if val_num1 != val_num2]

    if len(li_num1) != len(li_num2) or len(diff) != n_trans:
        return False, []

    else:
        return True, diff

# testing
n_replacement_away(13, 43, 1)  # 13, 23, 43, 53, 73, and 83
n_replacement_away(56003, 56113, 2)





