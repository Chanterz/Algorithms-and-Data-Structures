import time


class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print('elapsed time: %f ms' % self.msecs)


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


results = []
for i in range(0, 10 ** 8, 1000):
    a = [int(x) for x in str(i)]
    a.reverse()
    b = a.copy()

    with Timer() as t:
        multiplication(a, b)
    results.append(t.msecs)
    print(a, t.msecs)
while 0 in results:
    results.remove(0)
print(results)
print("done")
print("done")
