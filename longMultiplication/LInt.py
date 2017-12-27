import time
import matplotlib.pyplot as plt
import timeit


def multiplication(a, b):
    length = len(a) + len(b) + 1
    c = [0 for _ in range(length + 1)]
    for ix in range(len(a)):
        for jx in range(len(b)):
            c[ix + jx] += a[ix] * b[jx]

    for ix in range(length):
        c[ix + 1] += c[ix] // 10
        c[ix] %= 10
    return c


def multiplication_for_test(a):
    a = [int(x) for x in reversed(str(a))]
    length = len(a) * 2 + 1
    c = [0 for _ in range(length + 1)]

    for ix in range(len(a)):
        for jx in range(len(a)):
            c[ix + jx] += a[ix] * a[jx]

    for ix in range(length):
        c[ix + 1] += c[ix] // 10
        c[ix] %= 10
    return c

results = []

for i in range(1, 500):

    start = time.clock()
    multiplication_for_test(int("9"*i))
    end = time.clock()
    results.append(end - start)

plt.plot([x for x in range(1, 500)], results)
plt.grid(True)
plt.show()
