# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def pisano_period(m):
    a, b = 0, 1
    period = 0
    s = [0, 1]
    while not (a == 0 and b == 1) or period == 0:
        a, b = b, (a + b) % m
        period += 1
        s.append(b)
    return s[:-2]

def get_fibonacci_huge_fast(n, m):
    s = pisano_period(m)
    period = len(s)
    return s[n % period]


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    # print(pisano_period(2))
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_fast(n, m))
