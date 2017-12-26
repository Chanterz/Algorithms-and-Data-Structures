base = 10e9
first_num = [9, 9, 9, 9, 9]
second_num = [9, 9, 9, 9, 9]


def multiplication(a, b):
    length = len(a) + len(b) + 1
    c = [0 for _ in range(length+1)]

    for ix in range(len(a)):
        for jx in range(len(b)):
            c[ix + jx] += a[ix] * b[jx]

    for ix in range(length):
        c[ix + 1] += c[ix] // 10
        c[ix] %= 10

    while c[length - 1] == 0:
        length -= 1
    return c


print("".join(map(str, reversed(multiplication(first_num, second_num)))))
