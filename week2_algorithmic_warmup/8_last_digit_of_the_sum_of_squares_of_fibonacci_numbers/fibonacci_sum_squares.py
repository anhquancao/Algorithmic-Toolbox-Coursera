# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def pisano_period(m):
    a, b = 0, 1
    period = 0
    s = [0, 1]
    sum = 0
    while not (a == 0 and b == 1) or period == 0:
        a, b = b, (a + b) % m
        period += 1
        s.append(b)
    return s[:-2]

def fibonacci_sum_squares_fast(n):
    s = pisano_period(10)
    period = len(s)
    index = n % period
    current = s[index]
    previous = s[index - 1]
    return (current * (current + previous)) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_fast(n))
    # print(fibonacci_sum_squares_naive(n), fibonacci_sum_squares_fast(n))
