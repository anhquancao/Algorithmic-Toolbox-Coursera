#Uses python3

import sys
import itertools
import random

def is_greater_or_equal(a, b):
    return int(a + b) > int(b + a)

def largest_number(a):
    res = ""
    while len(a) != 0:
        # print(a)
        index = 0
        for i in range(1, len(a)):
            if is_greater_or_equal(a[i], a[index]):
                index = i

        res += a[index]
        a.pop(index)

    return res

# print(is_greater_or_equal('14','1'))
# print(is_greater_or_equal('21','2'))
def largest_number_naive(a):
    perms = list(itertools.permutations(a))
    perms = map(lambda x: int("".join(list(x))),perms)
    return max(perms)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

def stress_test(n, length):
    random.seed(1)
    while 1:
        a = []
        for i in range(n):
            number = "".join([str(random.randint(0,9)) for i in range(random.randint(1,length))])
            a.append(number)
        print("======")
        print(n)
        print(a)
        resNaive = int(largest_number_naive(a))
        res = int(largest_number(a))
        if resNaive == res:
            print("Ok")
        else:
            print("Wrong")
            print(resNaive)
            print(res)
            return

# stress_test(3,3)
# print(largest_number(['9','4','7']))
# print(largest_number_naive(['404','28','40']))
# print(is_greater_or_equal('40','404'))
# 14 1
# 21 2