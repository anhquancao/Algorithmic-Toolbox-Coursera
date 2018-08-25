# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    max_value = 0
    n = len(weights)
    # valuePerWeight = [(i, values[i] / weights[i]) for i in range(n)]
    # print(valuePerWeight)
    i = 0
    while i < n:
        i += 1
        if capacity == 0:
            return max_value
        # Find the max value per weight item
        max_index = 0

        for i in range(1, n):
            if weights[i] > 0 and values[i] / weights[i] > values[max_index] / weights[max_index]:
                max_index = i

        # Put it in the bag
        a = min(capacity, weights[max_index])
        max_value += a * (values[max_index] / weights[max_index])
        capacity -= a
        weights[max_index] -= a

    return max_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
