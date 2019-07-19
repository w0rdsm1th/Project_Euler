
"""
https://projecteuler.net/problem=52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

"""LEARNINGS
- didnt have to alter stride in search, was still quick
- 
"""

def same_digts(a, b):
    return sorted(str(a)) == sorted(str(b))

# test cases
same_digts(125874, 251748) is True
same_digts(125874, 51748) is False

def same_digts_6(x, x_2, x_3, x_4, x_5, x_6):
    return sorted(str(x)) == sorted(str(x_2)) == sorted(str(x_3)) == sorted(str(x_4)) == sorted(str(x_5)) == sorted(str(x_6))


def q52():
    x = 1
    while True:
        if same_digts_6(x, x*2, x*3, x*4, x*5, x*6):
            print("FOUND!: ", x)
            return x
        else:
            x += 1

if __name__ == '__main__':
    found = q52()
    # 142857





