# Uses python3
import sys

def get_fibonacci_last_digit_fast(n):
    a = [0, 1]
    i = 2
    while i <= n:
        lastDigit = (a[i - 1] + a[i - 2]) % 10
        a.append(lastDigit)
        i += 1
    return a[n]

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_fast(n))
