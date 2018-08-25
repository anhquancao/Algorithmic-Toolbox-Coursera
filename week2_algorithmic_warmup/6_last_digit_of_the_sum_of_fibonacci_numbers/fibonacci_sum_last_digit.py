# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

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
        sum = (sum + b) % m
    return s[:-2], sum


def fibonacci_sum_fast(n):
    if n == 0:
        return 0

    s, period_sum = pisano_period(10)
    period = len(s)
    return ((n // period) * period_sum + sum(s[: n % period + 1])) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # n = 100
    # print(fibonacci_sum_fast(n), fibonacci_sum_naive(n))
    print(fibonacci_sum_fast(n))

