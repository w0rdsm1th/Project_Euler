
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
import logging
import numba as nb
import collections as clcts

# going R to L down the indexes, (because that ensures will approach the smallest combination)
# keep that index constant
# check from smallest to largest if
# that number is not a complement
# if it is, what the smallest new substitute is (e.g. if 2 not viable, does 3 work? and is 3 already contained?)
# test outcome and update the complement set

"""LEARNINGS
- main: not cleaning up and simplifying the search space as we go. repeatedly trying 2, 3, 5, 7 over and over 
despite finding that "75" is not prime. QQ: how to determine which number to "eject"?
a given ejected number can appear in the final answer, just can't appear together!
 
- removing candidates (2, 5) from possible search space

n choose 5 

QQ how ensure that its "the lowest"? by incrementing

consider the first difference of all primes? increment the combinations gradually? 
"""


class Q60:
    """

    """
    def __init__(self, primes_list, upper_limit_index):
        # not really needed with new algorithm, they get filtered out by the repeated combination extensions
        # can filter 2, 5 from the search space, any number appended with 2 is even and with 5 is divisible by 5
        for bad in (2, 5):
            primes_list.remove(bad)

        self.primes_list = primes_list[:upper_limit_index]
        self.primes_set = set(primes_list)  # needs to be unlimited, considering concatenated primes
        # self.primes_map = dict(zip(range(self.num_primes), primes_list))
        self.large_search_prime = primes_list[upper_limit_index]

        self.good_combos = clcts.defaultdict(list)
        # {prime: [concatenated_pairs]}

    def _check_prime_pair(self, inp_prime_1, inp_prime_2):
        concated_num_1 = int(str(inp_prime_1) + str(inp_prime_2))
        concated_num_2 = int(str(inp_prime_2) + str(inp_prime_1))
        if concated_num_1 in self.primes_set and concated_num_2 in self.primes_set:
            self.good_combos[(inp_prime_1, )].append(inp_prime_2)
            return True

    def build_good_combos(self):
        for idx, each_prime in enumerate(self.primes_list):
            for other_prime in self.primes_list[:idx] + self.primes_list[idx+1:]:
                self._check_prime_pair(each_prime, other_prime)

            if idx % 100 == 0:
                print(f"build good combos just passed index {idx} and prime {each_prime}")

    @util.timer
    def find_combinations(self, threshold):
        previous_loop_dict = self.good_combos  # initialise
        for each_loop in range(threshold):
            loop_dict = {}
            for build_key, good_combos in previous_loop_dict.items():
                # ensure only incrementing combinations that meet threshold
                if good_combos:
                    for possible_key_extension in good_combos:
                        new_key = tuple(list(build_key) + [possible_key_extension])
                        loop_dict[new_key] = self._intersection(good_combos, possible_key_extension)

            # update the previous_loop_dict to new length
            previous_loop_dict = loop_dict

        return min([sum(keys) for keys, combos in previous_loop_dict.items()])

    def _intersection(self, building_tuple, possible_combos):
        return list(set.intersection(set(building_tuple), set(self.good_combos[(possible_combos, )])))



if __name__ == '__main__':
    # check = check_prime_pair_set([3, 7, 109, 673])
    # print(f"check status: {check}")

    prime_finder = util.PrimeFinder("util/primes.pickle")
    prime_list = prime_finder.read_prime_pickle()
    q60_solver = Q60(prime_list, 2_000)  # where 673 is index 121 so should solve for 4
    q60_solver.build_good_combos()
    answer = q60_solver.find_combinations(4)
    print(answer)



