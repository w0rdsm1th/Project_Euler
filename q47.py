
import util as ut
import math

"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. 
What is the first of these numbers?
"""
factors = ut.factors(644)
prime_factors = [fact for fact in factors if ut.is_prime(fact)]




def n_prime_factors(n, num_distinct_factors):

    def _check_prime_factors_multiply(num, prime_facts, new_prime_facts=None, prime_idx_to_exponent=0, exponent=2):
        product = ut.product(new_prime_facts) if new_prime_facts else ut.product(prime_factors)
        if product == num:
            return True

        # if smaller, for each of the prime factors, try increasingly higher powers UNTIL exceed
        elif product < num:
            if new_prime_facts:
                new_prime_facts = new_prime_facts[0:prime_idx_to_exponent] + [new_prime_facts[prime_idx_to_exponent]**exponent, ] + new_prime_facts[prime_idx_to_exponent+1:]

            else:
                new_prime_facts = prime_facts[0:prime_idx_to_exponent] + [prime_facts[prime_idx_to_exponent]**exponent, ] + prime_facts[prime_idx_to_exponent+1:]

            return _check_prime_factors_multiply(num, prime_facts, new_prime_facts, prime_idx_to_exponent, exponent+1)

        elif product > num and prime_idx_to_exponent+1 < len(prime_facts):
            # exceeded target number BUT still other
            return _check_prime_factors_multiply(num, prime_facts, new_prime_facts=None,
                                                 prime_idx_to_exponent=prime_idx_to_exponent+1, exponent=2)

        else:
            return False

    consecutive_ints = []
    while len(consecutive_ints) < num_distinct_factors:
        factors = ut.factors(n)

        # filter for prime factors and factors != n
        prime_factors = [fact for fact in factors if ut.is_prime(fact) if fact not in {1, n}]
        if len(prime_factors) == num_distinct_factors:
            check_outcome = _check_prime_factors_multiply(n, prime_factors)
            if check_outcome:
                consecutive_ints.append(n)
            else:
                consecutive_ints = []

        elif len(prime_factors) != num_distinct_factors and consecutive_ints:
            consecutive_ints = []

        n += 1
    return consecutive_ints


if __name__ == '__main__':
    consec_ints = n_prime_factors(210, 4)
    print(consec_ints)

