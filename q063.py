#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""DIFFICULTY RATING:
https://projecteuler.net/problem=63

Problem and explanation

The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?


"""

"""LEARNINGS:
- thinking about start criteria and not just bounding criteria, 
doing the first few in head and realising they don't converge:
2**2 == 4, then 2**3 == 8 and so diverges from being able to get to exponent = length of output
same for 3
different for 4 because 4**2 = 16 and immediately

len(str(3**999_999)) == 477_121
len(str(3**9_999_999)) == 4_771_213

len(str(4**999_999)) == 
len(str(4**9_999_999)) == 


- to numba JIT it need to impose mathematical length check
cannot use len(str())

- not re-calculating the exponent every time anew, instead can just cumulatively 
keep applying exponentiation to the base



instead use: if out // 10**curr_power:
(in case of out = 983, returns 0 if denominator curr_power is 3) 

consider the bounding: 
1) power bounding: for each possible base, at what point for n do they exceed their exponentiation limit?
e.g. for 2**10 = 1024 (len 4)
2**20=1_048_576 (len 7)
2**100=1267650600228229401496703205376 (len 31)
2**10000 = ... len 3011

Answer: keep going until the outcome exceeds the power


2) base bounding: at what base point does even squaring (minimum possible exponentiation) produce numbers of >2 digits?
answer: 10
cubing? ans: 10 again
method: take the minimum possible n+1 length number (100 for 2 and squaring) and then find 100**(1/

combine boundings to limit search space
e.g. increment the base until 
"""

import functools
import itertools
import util
import numba as nb


class q63:

    def __init__(self):
        self.answers = {}  # out: (base, exp)

    # @nb.jit(nopython=True)
    def answer(self):
        for curr_base in range(1, 11):
            print(f"checking base {curr_base}")
            curr_power = 1
            curr_out = curr_base**curr_power
            running_undershoot = curr_power - len(str(curr_out))
            while len(str(curr_out)) <= curr_power:
                # to numba-ify, to validate how would work
                # while not (curr_out // 10**curr_power):
                #     if curr_out // 10**curr_power == 0:
                if len(str(curr_out)) == curr_power:
                    self.answers[curr_out] = (curr_base, curr_power)

                curr_power += 1
                curr_out = curr_out*curr_base

                loop_undershoot = curr_power - len(str(curr_out))
                if loop_undershoot > running_undershoot:
                    print(f"undershoot stopping iter for {curr_base}, "
                          f"\ncurr_out: {curr_out}, curr_base: {curr_base}, curr_power: {curr_power}"
                          f"\nloop_undershoot: {loop_undershoot}, "
                          f"running_undershoot: {running_undershoot}")
                    break
                running_undershoot = loop_undershoot

            print(f"maxed out checking base with power: {curr_power}")



if __name__ == "__main__":
    answerer = q63()
    answerer.answer()
    print(len(answerer.answers.keys()))
