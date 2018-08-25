# Uses python3
def calc_fib(n):
    A = [0, 1]
    i = 2
    while i <= n:
        A.append(A[i - 1] + A[i - 2])
        i += 1
    return A[n]

n = int(input())
print(calc_fib(n))
