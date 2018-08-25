# Uses python3
from random import randint
import random

n = int(input())
A = [int(x) for x in input().split()]
random.seed(1)


def maxProductPairWiseNaive(n, A):
    product = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] * A[j] > product:
                product = A[i] * A[j]
    return product


def maxProductPairWiseFast(n, A):
    index1 = 0

    for i in range(1, n):
        if A[i] > A[index1]:
            index1 = i

    if index1 == 0:
        index2 = 1
    else:
        index2 = 0

    for i in range(1, n):
        if i != index1 and A[i] > A[index2]:
            index2 = i

    return A[index1] * A[index2]


def maxProductPairWise15n(n, A):
    if n == 2:
        return A[0] * A[1]
    if n == 3:
        maxIndex = 0
        for i in range(3):
            if A[i] > A[maxIndex]:
                maxIndex = i
        if maxIndex == 0:
            secondMaxIndex = 1
        else:
            secondMaxIndex = 0
        for i in range(3):
            if A[i] > A[secondMaxIndex] and i != maxIndex:
                secondMaxIndex = i
        return A[maxIndex] * A[secondMaxIndex]

    pairs = []

    for i in range(int(n / 2)):
        if (A[i * 2] > A[i * 2 + 1]):
            pairs.append((i * 2 + 1, i * 2))
        else:
            pairs.append((i * 2, i * 2 + 1))

    print(pairs)

    localMaxIndices = []
    for i in range(len(pairs)):
        p = pairs[i]
        if A[p[0]] > A[p[1]]:
            localMaxIndices.append(p[0])
        else:
            localMaxIndices.append(p[1])

    maxIndex = localMaxIndices[0]
    pairIndex = 0

    for index, i in enumerate(localMaxIndices):
        if A[i] > A[maxIndex]:
            maxIndex = i
            pairIndex = index

    print(maxIndex)

    if (maxIndex != localMaxIndices[0]):
        secondMaxIndex = localMaxIndices[0]
    else:
        secondMaxIndex = localMaxIndices[1]

    for i in localMaxIndices:
        if A[i] > A[secondMaxIndex] and i != maxIndex:
            secondMaxIndex = i

    print(pairs[pairIndex][0])
    if A[pairs[pairIndex][0]] > A[secondMaxIndex]:
        secondMaxIndex = pairs[pairIndex][0]

    if n % 2 == 1:
        if A[maxIndex] < A[-1]:
            secondMaxIndex = maxIndex
            maxIndex = -1
        elif A[secondMaxIndex] < A[-1]:
            secondMaxIndex = -1

    print(str(secondMaxIndex) + " " + str(maxIndex))

    return A[secondMaxIndex] * A[maxIndex]


def stressTest(N, M):
    while True:
        n = randint(2, N)
        A = [randint(0, M) for _ in range(n)]
        print("n: " + str(n))
        print("A: " + str(A))
        productNaive = maxProductPairWiseNaive(n, A)
        # productFast = maxProductPairWiseFast(n, A)
        productFast = maxProductPairWise15n(n, A)

        if productFast == productNaive:
            print("OK")
        else:
            print("Wrong: ")
            print("Product Naive: " + str(productNaive))
            print("Product Fast: " + str(productFast))
            return


stressTest(10, 5)
# print(maxProductPairWiseFast(n, A))
print(maxProductPairWise15n(n, A))
