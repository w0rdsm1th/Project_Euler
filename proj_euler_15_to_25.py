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
def is_prime(n):
    if n in [1, 2]:
        return True
    if n%2==0:
        return False
    else:
        if any(n%quots==0 for quots in range(2, n//2+1)):
            return False
        else:
            return True


def eul_quad(n):
    return n**2+n+41

def generic_quad(n, a, b):
    return n**2+a*n+b

res_list = (eul_quad(x) for x in range(0, 40))
res_list = (generic_quad(x, 1, 41) for x in range(0, 40))

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

res_list = all(is_prime(generic_quad(x, highest_alpha, highest_beta)) for x in range(0, 1012))

res_list




#_________________#_________________#_________________#_________________#_________________#_________________
#Q2
'''
'''

#_________________#_________________#_________________#_________________#_________________#_________________
#Q2
'''
'''



#_____________________________________________________________________________________________________________________