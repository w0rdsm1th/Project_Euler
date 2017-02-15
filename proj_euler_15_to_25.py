#
__author__ = 'Aleks Hughes'
import math
from pprint import pprint as print
import pandas as pd

#question 15 - lattice paths. finding
n=20
print(math.factorial((2*n))/math.factorial(n)**2)


def binom(n, m):
    b = [0] * (n + 1)
    b[0] = 1
    for i in range(1, n + 1):
        b[i] = 1
        j = i - 1
        while j > 0:
            b[j] += b[j - 1]
            j -= 1
    return b[m]
print(binom(40,20))

#question 16 - sum digits of 2**1000
print(sum(int(digit) for digit in str(2**1000)))

i = 0
for elem in str(2**1000):
    i += int(elem)
print(i)


#question 17 - Number letter counts
dict_spelled_out_nums = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
                         10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',
                         17:'seventeen', 18:'eighteen', 19:'nineteen',
                         20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}


def written_form_number(n, dict_spelled_out_nums):
    if n > 1000:
        return ValueError  # function only defined for '1000 and below ints'
    if n == 1000:
        return 'onethousand'

    if n//1000 != 0:
        return 'onethousand'

    if n//100 != 0:
        hundreds_place = n//100
        hundreds_word = dict_spelled_out_nums[hundreds_place]
        hundreds_word += 'hundred'
        n %= 100
        if n == 0:
            return hundreds_word
        if n <= 20:
            return hundreds_word + 'and' + dict_spelled_out_nums[n]
        else:
            tens_place = (n//10)%10
            tens_place *= 10  # restoring the total value of the extracted single int
            tens_word = dict_spelled_out_nums[tens_place]
            single_place = n%10
            single_word = dict_spelled_out_nums[single_place]  # ASSUMING that bc if a round number e.g. '30', single word will lookup '' in dict
            return hundreds_word + 'and' + tens_word + single_word
    if 20 < n <= 99:
        tens_place = (n // 10) % 10
        tens_place *= 10  # restoring the total value of the extracted single int
        tens_word = dict_spelled_out_nums[tens_place]
        single_place = n % 10
        single_word = dict_spelled_out_nums[single_place]  # ASSUMING that bc if a round number e.g. '30', single word will lookup '' in dict
        return tens_word + single_word
    if n <= 20:
        return dict_spelled_out_nums[n]

sum(len(written_form_number(n, dict_spelled_out_nums)) for n in range(0, 1001))

def recursive_prob17_solver(n, dict_spelled_out_nums):
    if n == 0:
        return ''
    return len(written_form_number(n, dict_spelled_out_nums)) + len(recursive_prob17_solver(n-1, dict_spelled_out_nums))


#----------------------------------------------------------------------------------------------------------------------
#q18 - max path of pyramid
raw_pyramid = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

cp = {}  # cp = 'cleaned pyramid'
row_number = 0
#rowXX : []
for elem in raw_pyramid.splitlines():
    cp[row_number] = [int(x) for x in elem.split()]
    row_number+=1

def max_path_frontier_bottom_up(tree):
    bottom_row_idx = max(tree.keys())
    output_tree_dict = tree.copy()
    while bottom_row_idx > 0:
        output_row = []
        for idx, each_elem in enumerate(output_tree_dict[bottom_row_idx-1]):
            output_row.append(each_elem+max(output_tree_dict[bottom_row_idx][idx], output_tree_dict[bottom_row_idx][idx+1]))
            output_tree_dict[bottom_row_idx-1] = output_row
        bottom_row_idx -= 1
    return output_tree_dict

max_path_frontier_bottom_up(cp)

#----------------------------------------------------------------------------------------------------------------------
#Q19 - How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.'''

month_days_dict = {
    1:['January', 31],
    2:['Feb_norm',28],
    3:['March', 31],
    4:['April', 30],
    5:['May', 31],
    6:['June', 30],
    7:['July', 31],
    8:['August', 31],
    9:['September', 30],
    10:['October', 31],
    11:['November', 30],
    12:['December', 31]}

def interval_leaps_calc(start_date, finish_date):
    sday = int(start_date.split('/')[0])
    smonth = int(start_date.split('/')[1])
    syr = int(start_date.split('/')[2])
    fday = int(finish_date.split('/')[0])
    fmonth = int(finish_date.split('/')[1])
    fyr = int(finish_date.split('/')[2])

    if syr % 4 == 0 and smonth <= 2 and not (syr % 100 == 0 and syr % 400 != 0):  # 'phantom' centennial leap years
        next_leap_year = syr
    else:
        next_leap_year = syr + 4 - (syr%4)

    if fyr % 4 == 0 and fmonth >= 3 and not (fyr % 100 == 0 and fyr % 400 != 0):
        final_candidate_leap_year = fyr
    else:
        final_candidate_leap_year = fyr - 4 + (fyr%4)

    output_leap_years = list(range(next_leap_year, final_candidate_leap_year+1, 4))
    return output_leap_years



def num_days_gap(start_date, finish_date, month_days_dict):
    '''start_date = dd/mm/yyyy, all ints
    '''
    sday = int(start_date.split('/')[0])
    smonth = int(start_date.split('/')[1])
    syr = int(start_date.split('/')[2])
    fday = int(finish_date.split('/')[0])
    fmonth = int(finish_date.split('/')[1])
    fyr = int(finish_date.split('/')[2])

    #calculate the gap
    gap_days = month_days_dict[smonth][1] - sday + fday
    gap_months = list(range(smonth+1, 13))+list(range(1, fmonth))
    gap_years_in_days_excl_leap = 365 * (fyr - syr - 1)
    gap_leap_years = interval_leaps_calc(start_date, finish_date)

    total_gap_days = gap_days + sum([month_days_dict[x][1] for x in gap_months]) + gap_years_in_days_excl_leap + len(gap_leap_years)
    return total_gap_days

def is_sunday(date, month_days_dict):
    if num_days_gap('7/1/1900', date, month_days_dict)%7== 0:
        return True
    else:
        return False

def generate_first_of_months_in_gap(start_date, finish_date):
    sday = int(start_date.split('/')[0])
    smonth = int(start_date.split('/')[1])
    syr = int(start_date.split('/')[2])
    fday = int(finish_date.split('/')[0])
    fmonth = int(finish_date.split('/')[1])
    fyr = int(finish_date.split('/')[2])

    if sday == 1:
        curr_month = smonth
    else:
        if smonth < 12:
            curr_month = smonth+1
            curr_year = syr
        else:
            curr_month = 1
            curr_year = syr+1

    while curr_month <= fmonth and curr_year <= fyr:
        generator_output = '/'.join(['1', str(curr_month), str(curr_year)])
        yield generator_output

        if curr_month == 12:
            curr_month = 1
            curr_year += 1
        else:
            curr_month += 1

sundays_long = []
for candidate_first_month in generate_first_of_months_in_gap('1/01/1901', '31/12/2000'):
    if is_sunday(candidate_first_month, month_days_dict):
        candidate_month = int(candidate_first_month.split('/')[-2])
        candidate_year = int(candidate_first_month.split('/')[-1])
        date_tuple = (1, candidate_month, candidate_year)
        sundays_long.append(date_tuple)
print(sundays_long)

import datetime
sundays_short = []
for year in range(1901, 2001):
    for month in range(1, 13):
        d = datetime.date(year, month, 1)
        if d.weekday() == 6:
            date_tuple = (1, d.month, d.year)
            sundays_short.append(date_tuple)
print(sundays_short)

#_____________________________________________________________________________________________________________________
import timeit
#Q20 - Factorial digit sum
def n_factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * n_factorial_recursive(n-1)

def n_factorial_while(n):
    output = 1
    while n>0:
        output *= n
        n -= 1
    return output

count_q20 = 0
for each_digit in str(n_factorial_recursive(100)):
    count_q20 += int(each_digit)
print(count_q20)

#_____________________________________________________________________________________________________________________
#Q21 - Amicable numbers
def proper_divisors(n):
    proper_divisors_output_list = [1]
    for candidate_divisor in range(2, int(n//2)+1):
        if n % candidate_divisor == 0:
            proper_divisors_output_list.append(candidate_divisor)
    return proper_divisors_output_list

def are_amicable(a, b):
    return sum(proper_divisors(a)) == sum(proper_divisors(b))

are_amicable(6, 6)

outputq21_list = []
outputq21_counter = 0
for x in range(0, 10001):
    if sum(proper_divisors(sum(proper_divisors(x)))) == x and x != sum(proper_divisors(x)):
        outputq21_list.append((x, sum(proper_divisors(x))))
        outputq21_counter += x + sum(proper_divisors(x))

outputq21_counter/2
print(outputq21_list)

#_____________________________________________________________________________________________________________________
#Q22 - names scores
import string

letter_alpha_score_dict = {}
for each_letter in string.ascii_uppercase:
    letter_alpha_score_dict[each_letter] = string.ascii_uppercase.index(each_letter)+1

def alphabetical_worth_name(given_name, letter_alpha_score_dict):
    output_counter = 0
    for each_letter in given_name:
        output_counter += letter_alpha_score_dict[each_letter]
    return output_counter

with open("C:\\Users\\IBM_ADMIN\\Documents\\2 - Project_Euler\\p022_names.txt", 'r') as f:
    q22_names_file = f.read()

q22_names_list = q22_names_file.split(',')
q22_names_list.sort()

alphabetical_worth_name(q22_names_list[0].strip('"'), letter_alpha_score_dict)

count_q22 = 0
for idx_name, each_name in enumerate(q22_names_list):
    count_q22 += alphabetical_worth_name(each_name.strip('"'), letter_alpha_score_dict) * (idx_name+1)
print(count_q22)

#_____________________________________________________________________________________________________________________
#Q23 - non-abundent sums
'''A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which CANNOT be written as the sum of two abundant numbers.'''
problem_set = range(0, 28123+1)

def is_abundant(n):
    return sum(proper_divisors(n)) > n

def array_has_2_candidates(A, arr_size, sum):
    l = 0
    r = arr_size - 1
    # traverse array for the two elements
    while l < r:
        if (A[l] + A[r] == sum):
            return True
        elif (A[l] + A[r] < sum):
            l += 1
        else:
            r -= 1
    return False

def limit_array_length(A, cut_off):
    while cut_off not in A:
        cut_off += 1
        if cut_off > A[-1]:
            return A
    if cut_off in A:
        return A[:A.index(cut_off)+1]

abundant_ints_in_problem_set_list = []
for candidate_abundant in problem_set:
    if is_abundant(candidate_abundant):
        abundant_ints_in_problem_set_list.append(candidate_abundant)

# dropping '0' from list of abundants
abundant_ints_in_problem_set_list = abundant_ints_in_problem_set_list[1:]

can_write_sum_abunds_list = []
for each_int in problem_set:
    if each_int%2 == 0 and each_int/2 in abundant_ints_in_problem_set_list:
        can_write_sum_abunds_list.append(each_int)
    else:
        # shortened_abundant_ints_in_problem_set_list = limit_array_length(abundant_ints_in_problem_set_list, each_int)
        if array_has_2_candidates(abundant_ints_in_problem_set_list,
                             len(abundant_ints_in_problem_set_list),
                             each_int):
            can_write_sum_abunds_list.append(each_int)
print('Done!')

abundant_ints_in_problem_set_list[0:10]
abundant_ints_in_problem_set_list[-10:]
is_abundant(28123)

can_write_sum_abunds_list[0:10]
array_has_2_candidates(abundant_ints_in_problem_set_list,
                             len(abundant_ints_in_problem_set_list),
                             28122)
array_has_2_candidates(abundant_ints_in_problem_set_list, len(abundant_ints_in_problem_set_list), 12)
is_abundant(12)
sum(can_write_sum_abunds_list)


sum(range(1,28124)) - sum(can_write_sum_abunds_list)
can_write_sum_abunds_list[-1]
#all ints in problem set that CANNOT be written as sum of two abundant numbers



#_____________________________________________________________________________________________________________________
#Q24 - Lexicographic permutations
'''
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

def get_pivot(li):
    last_elem = li[-1]
    for idx, elem in enumerate(li[::-1]):
        if elem < last_elem:
            break
        else:
            last_elem = elem
    return len(li) - idx - 1

def get_swap_candidate(li, piv_idx):
    if len(li[piv_idx:]) == 1:
        return len(li) - 1
    # compare to be swapped
    candidates = [x - li[piv_idx] for x in li[piv_idx:]]
    val, idx = min((val, idx) for (idx, val) in enumerate(candidates) if val > 0)
    return len(li[:piv_idx]) + idx

def lexicographic_perm(n):
    '''
    re-arrange input string to increase size by minimum increment
    :param n: string formatted number
    :return: string formatted, incremented number
    '''
    l_input = [int(x) for x in n]

    if sorted(l_input) == l_input[::-1]:
        print('Already maxed out, returning input')
        return n

    # find pivot
    piv_idx = get_pivot(l_input)
    # find the rightmost candidate to swap with the pivot
    swap_cand = get_swap_candidate(l_input, piv_idx)
    # perform swap and sort the suffix
    sorted_suffix = [str(x) for x in sorted(l_input[piv_idx:]) if x != l_input[swap_cand]]
    prefix = [str(x) for x in l_input[:piv_idx]]
    output = ''.join(prefix + [str(l_input[swap_cand])] + sorted_suffix)
    yield output

n = '0123456789'
counter = 1
while True:
    n = lexicographic_perm(n)
    counter+=1

    if counter == 1000000:
        break

    if counter % 1000 == 0:
        print(n)


#_____________________________________________________________________________________________________________________
#Q25 - 1000 length-digit Fibonacci number
'''The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?'''

def fib_generator():
    a, b, counter = 1, 0, 0
    while True:
        if len(str(a)) == 1000:
            return
        yield (counter, a)
        a, b = b, a+b
        # print('a: ', a, 'b: ', b, 'counter: ', counter)
        counter += 1

t = list(fib_generator())
t[-1][0]

#_____________________________________________________________________________________________________________________
#Q26 - Reciprocal cycles
'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

# remainders have benefit that IF recurs, will always then 'enter' the same cycle because dividing by the same
# denominator. e.g. if have remainer 1, next step is 10//7 which gives 1r3
# also have benefit

def write_recurring_dec(denom, numerator=1):
    output = {'dec':'', 'rems_list':[], 'cycle_period':None, 'cycle_flag':False}
    while True:
        if numerator % denom == 0:
            output['dec'] += str(numerator // denom)
            break
        output['dec'] += str(numerator // denom)
        remainder = numerator % denom

        if remainder not in output['rems_list']:
            output['rems_list'].append(remainder)
        elif remainder in output['rems_list']:
            output['cycle_flag'] = True
            output['cycle_period'] = len(output['rems_list']) - output['rems_list'].index(remainder)
            break
        numerator = (numerator % denom)*10
    return output

# what about remainders for first dec place??

m = write_recurring_dec(999)
t = write_recurring_dec(7)
t = write_recurring_dec(6)
n = write_recurring_dec(10)
write_recurring_dec(6)
len(n[0])
len(t[0])

max_cycle = 1
max_cycle_denom = 6
for denom in range(6, 999):
    cycle_check = write_recurring_dec(denom)
    if cycle_check['cycle_flag']:
        if cycle_check['cycle_period'] > max_cycle:
            max_cycle = cycle_check['cycle_period']
            max_cycle_denom = denom
print(max_cycle_denom)


#_________________#_________________#_________________#_________________#_________________#_________________
#Q27
'''
Euler discovered the remarkable quadratic formula:

n**2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
However, when n=40,40**2+40+41=40(40+1)+41n=40,40**2+40+41=40(40+1)+41 is divisible by 41, and certainly when
 n=41,41**2+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601n2−79n+1601 was discovered, which produces 80 primes for the
consecutive values 0≤n≤790≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n**2+an+b, where |a|<1000|a|<1000 and |b|≤1000|b|≤1000

where |n||n| is the modulus/absolute value of nn
e.g. |-11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
'''
from math import ceil

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2==0 or n%3==0:
        return False
    else:
        if any(n%divisors==0 or n%(divisors+2)==0 for divisors in range(5, ceil(n**0.5)+1, 2)):
            return False
        else:
            return True

def eul_quad(n):
    return n**2+n+41

def generic_quad(n, a, b):
    return n**2+a*n+b

res_list = (eul_quad(x) for x in range(0, 40))
res_list = (generic_quad(x, 1, 41) for x in range(0, 40))
all(is_prime(generic_quad(x, -79, 1601)) for x in range(0, 81))

# for combo of a and b, check from n=0 if values produced are prime, find the largest such value of n that this still true
highest_consec_primes = 0
highest_alpha, highest_beta = None, None
for beta in range(-1001, 1001):
    for alpha in range(-1000, 1000):
        n = 0
        while True:
            quad_out = generic_quad(n, alpha, beta)
            if not is_prime(quad_out):
                break
            if n > highest_consec_primes:
                highest_alpha, highest_beta, highest_consec_primes = alpha, beta, n
            n+=1

print('highest_alpha: ', highest_alpha, '\n',
      'highest_beta: ', highest_beta, '\n',
      'answer: ', highest_alpha*highest_beta)

all(is_prime(generic_quad(x, highest_alpha, highest_beta)) for x in range(0, highest_consec_primes+1))




#_________________#_________________#_________________#_________________#_________________#_________________
#Q28 - Number spiral diagonals
'''Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''
# start with i, j = 0, 0
# ahead steps = 1, forms a 2x2 square
# goes forward 1 in +i or -i direction to increment size of square, 90deg right turn, completes ahead steps, 90deg right turn, ahead steps

def recur_spiral(i, j, ahead_steps, spiral_num, diag_elem_sum, heading='E'):
    heading_dict = {'E':1, 'W':-1}
    assert heading in heading_dict.keys()
    head_multiplier = heading_dict.pop(heading)

    i += 1 * head_multiplier
    spiral_num += 1
    if heading == 'W':
        assert abs(i) == abs(j)
        diag_elem_sum += spiral_num

    j -= ahead_steps * head_multiplier
    spiral_num += ahead_steps
    assert abs(i) == abs(j)
    # print('abs(i): ', abs(i),  'abs(j): ', abs(j), 'spiral: ', spiral_num)
    diag_elem_sum += spiral_num  # lead diagonal elems

    i -= ahead_steps * head_multiplier
    spiral_num += ahead_steps

    if abs(i) == abs(j):
        diag_elem_sum += spiral_num

    new_heading = list(heading_dict.keys())[0]
    ahead_steps+=1
    output_dict = {'i':i, 'j':j, 'ahead_steps':ahead_steps, 'spiral_num':spiral_num,
                   'diag_elem_sum':diag_elem_sum, 'heading':new_heading}

    return output_dict

spiral_dict = recur_spiral(0, 0, 1, 1, diag_elem_sum=1, heading='E')

while True:
    spiral_dict = recur_spiral(**spiral_dict)
    if spiral_dict['ahead_steps'] >= 1001:
        break
print(spiral_dict['diag_elem_sum'])



#_________________#_________________#_________________#_________________#_________________#_________________
#Q29
'''
'''
len(set((a**b for a in range(2, 101) for b in range(2, 101))))

#_________________#_________________#_________________#_________________#_________________#_________________
#Q30
'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

# Q: what is the limit case?? how do we know to stop checking numbers??
# 1**5 not included because not a sum

def sum_powers_digits(n, power):
    assert type(n) == int and len(str(n)) >= 2  # input is type int and can sum the parts
    output = sum(int(dig)**power for dig in str(n))
    return output

sum_powers_digits(194979, 5)

t = list((x for x in range(10, 999999) if x == sum_powers_digits(x, 5)))
sum(t)

#_________________#_________________#_________________#_________________#_________________#_________________
#Q31 Coin Sums
'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

list_co = [1, 2, 5, 10, 20, 50, 100, 200]
def recur_q31(list_coins, change_objective):
    if change_objective == 0:
        return 1
    elif change_objective < 0 or len(list_coins) == 0:
        return 0
    else:
        biggest_coin = sorted(list_coins)[-1]
        rest_coins = sorted(list_coins)[:-1]
        return recur_q31(list_coins, change_objective-biggest_coin) + recur_q31(rest_coins, change_objective)

recur_q31(list_co, 200)


#_________________#_________________#_________________#_________________#_________________#_________________
#Q32 - Pandigital products
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
123456789
import itertools

def q32_check_pandigital_mults(string_pandigital):
    output_dict = {}

    for equals_spot in range(2, 9):
        for mult_spot in range(1, equals_spot):
            a = int(string_pandigital[:mult_spot])
            b = int(string_pandigital[mult_spot:equals_spot])
            c = int(string_pandigital[equals_spot:])
            if a * b == c:
                output_dict[str(c)] = sorted([a, b])
    if output_dict:
        return output_dict
    else:
        return False

q32_results = {}
for each_pan in itertools.permutations(range(1, 10)):
    temp_res = q32_check_pandigital_mults(''.join(str(x) for x in each_pan))
    if temp_res:
        for each_c_result in temp_res.keys():
            if each_c_result not in q32_results.keys():
                q32_results[each_c_result] = temp_res[each_c_result]

sum(int(x) for x in q32_results.keys())


#_________________#_________________#_________________#_________________#_________________#_________________
#Q33
'''The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
49/98

q33_dub_digit_combos = list(x for x in itertools.product(range(0, 10), repeat=2) if x[0] != 0)

def q33_check_naive_cancel(numerator, denominator):
    output_list = []
    actual_frac = int(''.join(str(x) for x in numerator)) / int(''.join(str(x) for x in denominator))

    if numerator[0] == denominator[0] and numerator[0] != 0 and denominator[1] != 0 and numerator[1] / denominator [1] == actual_frac:
        output_list.append(''.join(str(x) for x in numerator) + '/' +''.join(str(x) for x in denominator))
    if numerator[1] == denominator[1] and numerator[1] != 0 and denominator[0] != 0 and numerator[0] / denominator[0] == actual_frac:
        output_list.append(''.join(str(x) for x in numerator) + '/' +''.join(str(x) for x in denominator))

    if numerator[0] == denominator[1] and numerator[1] != 0 and denominator[0] != 0 and numerator[1] / denominator[0] == actual_frac:
        output_list.append(''.join(str(x) for x in numerator) + '/' +''.join(str(x) for x in denominator))
    if numerator[1] == denominator[0] and numerator[0] != 0 and denominator[1] != 0 and numerator[0] / denominator[1] == actual_frac:
        output_list.append(''.join(str(x) for x in numerator) + '/' +''.join(str(x) for x in denominator))

    return output_list

q33_check_naive_cancel((4, 9), (9, 8))

[3, 4, 5]
[3, 4, 5][1:]

q33_res = []
for q33_d_idx, q33_denom in enumerate(sorted(q33_dub_digit_combos)):
    for q33_numerator in q33_dub_digit_combos[:q33_d_idx]:
        temp_res = q33_check_naive_cancel(q33_numerator, q33_denom)
        if temp_res:
            q33_res.extend(temp_res)

print(q33_res)
len(q33_res)
q33_ans = 1
[q33_ans*int(x) for x in q33_res]
16/64*26/65*19/95*49/98


#_________________#_________________#_________________#_________________#_________________#_________________
#Q34
'''145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
import math

for n in range(3, 10000000000):
    if sum(math.factorial(int(x)) for x in str(n)) == n:
        print(n)

145+40585

#_________________#_________________#_________________#_________________#_________________#_________________
#Q35
'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''
q35_all_rotations_prime(197)
q35_all_rotations_prime(140)

q_35_circ_primes_list = []
for n in range(100, 1000001):
    s = str(n)
    if all(is_prime(int(s[x:] + s[:x])) for x in range(len(s))):
        q_35_circ_primes_list.append(s)

print(13+len(q_35_circ_primes_list))

len(list(s for s in range(100, 1000001) if all(is_prime(int(str(s)[x:] + str(s)[:x])) for x in range(len(str(s))))))
#_________________#_________________#_________________#_________________#_________________#_________________
#Q36
'''The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
"{0:b}".format(585)  # without the '0b' in front

sum(n for n in range(1000001) if str(n) == str(n)[::-1] and "{0:b}".format(n) == "{0:b}".format(n)[::-1])



#_________________#_________________#_________________#_________________#_________________#_________________
#Q37
'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
string_n = '3793'
def q38_truncatable_prime_front(string_n):
    n = int(string_n)
    if n < 10:
        return is_prime(n)

    else:
        return is_prime(n) and q38_truncatable_prime_front(string_n[1:])

def q38_truncatable_prime_back(string_n):
    n = int(string_n)
    if n < 10:
        return is_prime(n)
    else:
        return is_prime(n) and q38_truncatable_prime_back(string_n[:-1])

# t = list(is_prime(int(str(n)[x:])) and is_prime(int(str(n)[:-y])) for n in range(9, 10000000, 2) for x in range(len(str(n))) for y in range(1, len(str(n))))

target_set = (n for n in range(9, 10000000, 2) if is_prime(n))

q38_output = []
for _ in target_set:
    if all(is_prime(int(str(_)[x:])) for x in range(len(str(_)))) and all(is_prime(int(str(_)[:-y])) for y in range(1, len(str(_)))):
        q38_output.append(_)
print(q38_output)
len(q38_output)
sum(q38_output)

#_________________#_________________#_________________#_________________#_________________#_________________
#Q38
'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

def is_pandigital(n):
    return sorted(set(str(n))) == sorted(set('0123456789'))

is_pandigital('123456789')
is_pandigital('1234589')

# simple, no generators
q38_prods = (1, 2)
q38_highest_seen = 918273645
q38_highest_prods = {'prods':(1, 2, 3, 4, 5), 'mult':9}
q38_curr = 0

q38_stop_crit1 = 987654321
q38_stop_crit2 = (1, 2, 3, 4, 5, 6, 7, 8)

n = 1
while True:
    n+=1
    concat_prod = int(''.join((str(x) for x in (n*y for y in q38_prods))))
    if is_pandigital(concat_prod):
        if concat_prod > q38_highest_seen:
            q38_highest_prods['prods'] = q38_prods
            q38_highest_prods['mult'] = n

    if concat_prod > q38_stop_crit1:
        # incrementing the product set, starting multiplier search again
        q38_prods += (q38_prods[-1]+1, )
        n = 1

    if q38_prods == q38_stop_crit2:
        print('DONE SEARCH, highest found: {}'.format(int(''.join((str(x) for x in (q38_highest_prods['mult']*y for y in q38_highest_prods['prods']))))))
        break



#_________________#_________________#_________________#_________________#_________________#_________________
#Q39
'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''
q39_highest_p = 3
q39_highest_p_solutions = []

for p in range(3, 1001):
    solutions = list(((p-c-b), b, c, p) for c in range(1, p) for b in range(1, p-c) if
                     (p - c - b) ** 2 + b ** 2 == c ** 2)
    if len(solutions) > len(q39_highest_p_solutions):
        q39_highest_p = p
        q39_highest_p_solutions = solutions
    if p%100 == 0:
        print('current p: ', p)
print('DONE highest found: ', q39_highest_p)



#_________________#_________________#_________________#_________________#_________________#_________________
#Q40
'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''
# q40_idx_list = [1, 10, 100, 1000, 10000, 100000, 1000000]

q40_idx_list = [10**n for n in range(7)]

def q40_concat_count_fraction(frac, next_int, q40_idx_list_input):
    while True:
        frac = str(frac) + str(next_int)
        next_int+=1
        if len(str(frac)) > q40_idx_list_input[-1]+1:
            break
    return([str(frac)[_+1] for _ in q40_idx_list_input])



[int(x) for x in q40_concat_count_fraction(0.1, 2, q40_idx_list)]
1*1*5*3*7*2*1

#_________________#_________________#_________________#_________________#_________________#_________________
#Q41
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
import itertools
q41_stop_crit1 = 987654321  # obvious ceiling value to search to - largest odd pandigital


any(is_prime(int(''.join([str(_) ])) for _ in n for n in perms))

t = [n for n in perms[::-1] for _ in n if is_prime(int(''.join(str(_))))][0]

q41_all_dig = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while True:
    perms = list(itertools.permutations(q41_all_dig))
    for each_num in perms[::-1]:
        int_each_num = int(''.join([str(_) for _ in each_num]))
        if is_prime(int_each_num):
            print(int_each_num)
            break
    q41_all_dig = q41_all_dig[:-1]
    if len(q41_all_dig) == 2:
        break


#_________________#_________________#_________________#_________________#_________________#_________________
#Q42
'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''
import string
from math import ceil
q42_file = r"C:\Users\IBM_ADMIN\Documents\2 - Project_Euler\p042_words.txt"


def q42_word_value(word_string):
    return sum(string.ascii_uppercase.index(_.upper())+1 for _ in word_string)

def q42_increment_tri_nums(stop_int):
    stop_range = ceil((-1+(1+8*stop_int)**.5)/2)  # using quadratic formula to solve for
    return [int(0.5*(_+1)*(_+2)) for _ in range(stop_range)]

with open(q42_file, 'r') as f:
    q42_all_file_words = [word.strip('"') for line in f for word in line.split(',')]
    tri_num_series = [1, 3]
    tri_word_counter = 0
    non_tri_word_counter = 0
    for each_word in q42_all_file_words:
        curr_word_value = q42_word_value(each_word)

        if curr_word_value > tri_num_series[-1]:
            old_tri_num_series_limit = tri_num_series[-1]
            tri_num_series = q42_increment_tri_nums(curr_word_value)
            print('incremented tri_nums, from {} to {}'.format(old_tri_num_series_limit, tri_num_series[-1]))

        if curr_word_value in tri_num_series:
            tri_word_counter+=1

        if curr_word_value not in tri_num_series:
            non_tri_word_counter+=1

    assert non_tri_word_counter + tri_word_counter == len(q42_all_file_words)
    print('Done! total number of triangular words: ', tri_word_counter)

#_________________#_________________#_________________#_________________#_________________#_________________
#Q43
'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''

# substrings are divisible by incrementing primes
from itertools import permutations

def is_pandigital_0to9(n):
    return sorted(set(str(n))) == sorted(str(n)) == sorted('0123456789')

def q43_substr_division(n):
    # assert is_pandigital_0to9(n)
    divs = (2, 3, 5, 7, 11, 13, 17)
    # list(int(str(n)[div_idx:][1:4]) for div_idx, each_div in enumerate(divs))
    all(int(str(n)[div_idx:][1:4]) % each_div == 0 for div_idx, each_div in enumerate(divs))

def q43_concat_tuple(tup_input):
    s = ''.join(map(str, tup_input))
    return int(s)

q43_concat_tuple((9, 8, 1, 4, 5, 0, 6, 2, 3, 7))

q43_ans = sum(q43_concat_tuple(_) for _ in permutations(range(0, 10)) if q43_substr_division(q43_concat_tuple(_)))





#_________________#_________________#_________________#_________________#_________________#_________________
#Q44
'''
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
'''
%pylab
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 2000.0, 1)
y = 0.5*x*(3*x - 1)
plt.plot(x, y)

# sum AND difference are pentagonal
# ie the solution is a whole number IF plugged into the pentagonal quadratic
# the difference abs(pj - pk) is minimised
q44_demo_cannot_use_quadratic1 = 12
q44_demo_cannot_use_quadratic2 = 13
(1+(24*q44_demo_cannot_use_quadratic1)**.5)/6
(1+(24*q44_demo_cannot_use_quadratic2)**.5)/6


from math import ceil
from datetime import datetime

from itertools import combinations
from operator import itemgetter  # to be able to 'extract' items from tuples nested in lists


def q44_check_pentagonal(input_int, pent_tuple):
    assert isinstance(input_int, int) and input_int%1 == 0
    if input_int > pent_tuple[-1]:
        q44_stop_crit = ceil((1+(24*input_int)**.5)/6)
        assert len(pent_tuple) <= q44_stop_crit
        pent_tuple = pent_tuple + tuple(int(0.5 * _ * (3 * _ - 1)) for _ in range(len(pent_tuple) + 1, q44_stop_crit + 1))
    return (input_int in pent_tuple, pent_tuple)

q44_check_pentagonal(1000, t)
q44_check_pentagonal(1926, t)
q44_check_pentagonal(92, t)
q44_check_pentagonal(48, t)
q44_check_pentagonal((22 + 70), t)


def q44_check_diff_pentagonal(pj_pk_comb, pent_tuple):
#     assert isinstance(pj_pk_comb[0], int) and isinstance(pj_pk_comb[1], int)
    return abs(pj_pk_comb[0] - pj_pk_comb[1]) in pent_tuple

def q44_pent_generator():
    n = 0
    while True:
        yield int(0.5 * n * (3 * n - 1))
        n+=1

# for a new pentagonal:
# check if difference with each of the other, pre-created pentagonals is pentagonal
# if yes, create sum of both pentagonals and store
# at intervals, check the sums created to see if pentagonal (if contained in list)

pent_tuple = tuple(int(0.5 * _ * (3 * _ - 1)) for _ in range(1, 10000))
tlong_combo_diffs = ((abs(_[0] - _[1]), _) for _ in combinations(pent_tuple, 2))
tlong_combo_sums = ((_[0] + _[1], _) for _ in combinations(pent_tuple, 2))

tlong_combo_diffs_filtered = (_ for _ in tlong_combo_diffs if _[0] in pent_tuple)
tlong_combo_sums_filtered = (_ for _ in tlong_combo_sums if _[0] in pent_tuple)

tlong_sums = (_[1] for _ in tlong_combo_diffs_filtered)
tlong_diffs = (_[1] for _ in tlong_combo_sums_filtered)

q44_in_both = [_ for _ in tlong_sums if _ in tlong_diffs]

tlong_combo_diffs.sort(key=itemgetter(0))



pent_tuple[-1]
pent_tuple[-1] - pent_tuple[70000] * 2
gen = q44_pent_generator()
new_pent = next(gen)

new_pent = next(gen)

t_lower_limit, t_upper_limit = 999, 2000
t = tuple(int(0.5 * _ * (3 * _ - 1)) for _ in range(t_lower_limit, t_upper_limit+1))
q44_diff_combs = [(combs, abs(combs[0] - combs[1]), combs[0]+combs[1]) for combs in combinations(t, 2) if abs(combs[0] - combs[1])in t]



# plan: for pentagonal series 2-combinations, calc their difference, if diff itself pentagonal, record
# with recorded differences, sort so that lowest diff combination is first
# plot behaviour of combinations as difference decreases (3d space??)
# find first combination in series of tuples that have pentagonal sum

pre = datetime.now()
q44_diff_combs = [(combs, abs(combs[0] - combs[1]), combs[0]+combs[1]) for combs in combinations(pent_tuple, 2) if
                  abs(combs[0] - combs[1]) in pent_tuple and combs[0] + combs[1] in pent_tuple]
post = datetime.now()
print(post - pre)

'''
LESSONS LEARNED
1. rounding error quickly renders mathematical checking of actual numbers inaccurate. (e.g. quadratic formula on large numbers)

2. dont use type(something) == int, use isinstance(something, int)


'''

#_________________#_________________#_________________#_________________#_________________#_________________
#Q45
'''

'''

'''
LESSONS LEARNED
1.

2.

'''

#_________________#_________________#_________________#_________________#_________________#_________________
#Q46
'''

'''

'''
LESSONS LEARNED
1.

2.

'''
#_________________#_________________#_________________#_________________#_________________#_________________
#Q47
'''

'''


'''
LESSONS LEARNED
1.

2.

'''
#_________________#_________________#_________________#_________________#_________________#_________________
#Q48
'''

'''



'''
LESSONS LEARNED
1.

2.

'''
#_________________#_________________#_________________#_________________#_________________#_________________
#Q49
'''

'''



'''
LESSONS LEARNED
1.

2.

'''
#_________________#_________________#_________________#_________________#_________________#_________________
#Q5
'''

'''


'''
LESSONS LEARNED
1.

2.

'''

#_________________#_________________#_________________#_________________#_________________#_________________
#Q5
'''

'''



'''
LESSONS LEARNED
1.

2.

'''
#_________________#_________________#_________________#_________________#_________________#_________________
#Q5
'''

'''



'''
LESSONS LEARNED
1.

2.

'''
#_________________#_________________#_________________#_________________#_________________#_________________
#Q5
'''

'''



'''
LESSONS LEARNED
1.

2.

'''
#_________________#_________________#_________________#_________________#_________________#_________________
#Q5
'''

'''



'''
LESSONS LEARNED
1.

2.

'''
#_________________#_________________#_________________#_________________#_________________#_________________
#Q5
'''

'''



'''
LESSONS LEARNED
1.

2.

'''