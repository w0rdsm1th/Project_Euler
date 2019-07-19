
"""
DIFFICULTY RATING: 5%
https://projecteuler.net/problem=55

Lychrel numbers

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

"""
import functools

"""LEARNINGS
- using map() with kwargs, functools.partial():
https://stackoverflow.com/questions/13499824/using-map-function-with-keyword-arguments
see Martijn Peters's answer here https://stackoverflow.com/a/13499853/3596968

- using inbuilt filter to filter for numbers in range that ARE Lychrel
https://book.pythontips.com/en/latest/map_filter.html#filter
"""


# 10677 - requires 53 iterations

def check_lychrel(inp_num, max_attempts=50, verbose=False):
    attempt_count = 1
    loop_num = inp_num

    while attempt_count < max_attempts:
        loop_num += int(str(loop_num)[::-1])
        if loop_num == int(str(loop_num)[::-1]):
            if verbose:
                print("N='{0}' is not Lychrel, after {1} attempts".format(inp_num, attempt_count))
            return False

        attempt_count += 1
        if attempt_count % 10 == 0 and verbose:
            print("attempt count: ", attempt_count)

    print("N='{0}' is Lychrel, after {1} attempts".format(inp_num, attempt_count))
    return True

# 47: after 1 iteration
# 349: after 3 iterations
# 196: "never" converges >> *is Lychrel*
# 10_677: first number to require over 50 iterations to show (requires 53)


check_lychrel_verbose = functools.partial(check_lychrel, verbose=True)
check_lychrel_verbose_100attempts = functools.partial(check_lychrel, max_attempts=100, verbose=True)
# test_case_map = list(map(check_lychrel_verbose_100attempts, [47, 349, 196, 10_677]))

if __name__ == '__main__':
    t = list(filter(check_lychrel, range(10, 10_001)))
    print("Lychrels found: ", t)
    print("number of Lychrels found: ", len(t))
    # test_case0 = check_lychrel_verbose(9, verbose=True)
    # test_case1 = check_lychrel(47, verbose=True)
    # test_case2 = check_lychrel(349, verbose=True)
    # test_case3 = check_lychrel(196, verbose=True)
    # test_case4 = check_lychrel(10_677, verbose=True)

    # t = list(filter(check_lychrel, range(10, 10_000)))
    # t = list(filter(check_lychrel, range(10, 200)))



