#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
convenience class to write list of primes to pickle

intention of making it seamless to increment by time or search ceiling
"""
import os
import pickle
import datetime as dt

import functools
import itertools
import util


class PrimeFinder:

    def __init__(self, pickle_name: str = "primes.pickle",):
        self.out_pickle_name = pickle_name
        self.ceiling = None
        self.timelimit_seconds = None

    def read_prime_pickle(self):
        with open(self.out_pickle_name, 'rb') as f:
            prime_list = pickle.load(f)
        return prime_list

    def prime_diagnostics(self):
        prime_list = self.read_prime_pickle()
        print(f"pickle len {len(prime_list):,.0f}")
        print(f"largest prime in pickle {prime_list[-1]:,.0f}")
        last_digits = set([str(_)[-1] for _ in prime_list])
        print(f"last digits of primes in file: {last_digits}")

    def find_primes(self, ceiling: int = None,
                    timelimit_seconds: int = None):
        if not ceiling and not timelimit_seconds:
            print("gotta supply one of ceiling or ")
            return None
        self.ceiling = ceiling
        self.timelimit_seconds = timelimit_seconds

        # if pickle exists read it and get starting point
        if os.path.isfile(self.out_pickle_name):
            self._add_to_prime_pickle()

        # if doesnt exist then create
        else:
            self._create_prime_pickle()

    def _create_prime_pickle(self):
        prime_list = [2, ] + self._find_new_primes(3)
        with open(self.out_pickle_name, 'wb') as f:
            pickle.dump(prime_list, f)

    def _add_to_prime_pickle(self):
        already_found_primes = self.read_prime_pickle()
        start_prime = already_found_primes[-1]
        print(f"prime pickle found, starting prime {start_prime:,.0f}")

        prime_list = self._find_new_primes(start_prime)
        out_list = already_found_primes + prime_list

        with open(self.out_pickle_name, 'wb') as f:
            pickle.dump(out_list, f)

    def _find_new_primes(self, start_prime):
        if self.ceiling:
            prime_list = self.find_primes_ceiling(start_prime, self.ceiling)
        elif self.timelimit_seconds:
            prime_list = self.find_primes_timelimit(start_prime, self.timelimit_seconds)

        return prime_list

    def find_primes_ceiling(self, starting_prime, ceiling) -> list:
        out_list = []
        for current_candidate in range(starting_prime, ceiling, 2):
            if util.is_prime(current_candidate):
                out_list.append(current_candidate)

        print("search ceiling exceeded, primes found this run {0:,.0f}".format(len(out_list)))
        return out_list

    def find_primes_timelimit(self, starting_prime, timelimit_seconds) -> list:
        start_time = dt.datetime.now()
        print(f"find primes timelimit start time: {start_time.strftime('%H:%m')}")

        current_candidate = starting_prime + 2
        out_list = []
        while (dt.datetime.now() - start_time).seconds < timelimit_seconds:
            if util.is_prime(current_candidate):
                out_list.append(current_candidate)

            current_candidate += 2

        print("search time limit exceeded, primes found this run {0:,.0f}".format(len(out_list)))
        return out_list


if __name__ == "__main__":
    prime_finder = PrimeFinder()
    # prime_finder.find_primes(ceiling=100_000_000)
    # prime_finder.find_primes(timelimit_seconds=30)

    prime_finder.prime_diagnostics()


