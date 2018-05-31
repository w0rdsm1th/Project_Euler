### template question imports
import util as ut
import math

"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""

def exponent_sum(start, end, suffix_len):
    return str(sum((in_**in_ for in_ in range(start, end+1))))[-suffix_len:]



if __name__ == '__main__':
    assert(exponent_sum(1, 10, len('10405071317') == '10405071317'))
    print(exponent_sum(1, 1000, 10))





