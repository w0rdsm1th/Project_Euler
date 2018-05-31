
import util as ut
import math

"""
https://projecteuler.net/problem=627

Counting products
Consider the set S of all possible products of n positive integers not exceeding m, that is
S={x1x2…xn|1≤x1,x2,...,xn≤m}.
Let F(m,n) be the number of the distinct elements of the set S.
For example, F(9,2)=36 and F(30,2)=308.

Find F(30,10001) mod 1000000007.

"""

factors = ut.factors(9)



def fun_F(m, n):
    # 1*1
    factors = ut.factors(m)
    pass


if __name__ == '__main__':
    modulus = 1_000_000_007

