# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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


def fibonacci_partial_sum_fast(from_, to):
    if to == 0:
        return 0

    s, period_sum = pisano_period(10)
    period = len(s)

    num_periods = to // period - from_ // period
    return (num_periods * period_sum + sum(s[from_ % period: to % period + 1])) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))
    # print(fibonacci_partial_sum_naive(from_, to), fibonacci_partial_sum_fast(from_, to))
