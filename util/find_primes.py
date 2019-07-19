#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
convenience method to write list of primes to pickle

"""
import os
import pickle
import datetime as dt
import numba as nb

import functools
import itertools
import util


class PrimeFinder:
    def __init__(self, search_ceiling: int = None, search_timelimit_seconds: int = None):
        self.out_pickle_name = "primes.pickle"
        self.ceiling = search_ceiling
        self.timelimit_seconds = search_timelimit_seconds

    def read_prime_pickle(self):
        with open(self.out_pickle_name, 'rb') as f:
            prime_list = pickle.load(f)
        return prime_list

    def prime_diagnostics(self):
        prime_list = self.read_prime_pickle()
        print(f"pickle len {len(prime_list):,.0f}")
        print(f"largest prime in pickle {prime_list[-1]:,.0f}")

    def find_primes(self):
        # if pickle exists read it and get starting point
        if os.path.isfile(self.out_pickle_name):
            self._add_to_prime_pickle()

        # if doesnt exist then create
        else:
            self._create_prime_pickle()

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
        while True:
            if util.is_prime(current_candidate):
                out_list.append(current_candidate)

            current_candidate += 2

            if (dt.datetime.now() - start_time).seconds > timelimit_seconds:
                break

        print("search time limit exceeded, primes found this run {0:,.0f}".format(len(out_list)))
        return out_list

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


if __name__ == "__main__":
    # prime_finder = PrimeFinder(search_ceiling=10_000_000)
    # prime_finder = PrimeFinder(search_timelimit_seconds=60)
    # prime_finder.find_primes()

    prime_finder = PrimeFinder()
    prime_finder.prime_diagnostics()


