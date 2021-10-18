from builtins import range, print
from timeit import Timer

memo = {0: 0, 1: 1}


def fibm(n):
    if not n in memo:
        memo[n] = fibm(n - 1) + fibm(n - 2)
        # print(memo)
    return memo[n]


def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


for i in range(1, 30):
    s = "fibm(" + "{}".format(i) + ")"
    t1 = Timer(s, "from __main__ import fibm")
    time1 = t1.timeit(3)
    s = "fibi(" + "{}".format(i) + ")"
    t2 = Timer(s, "from __main__ import fibi")
    time2 = t2.timeit(3)
    print("n=%2d, fibm: %8.6f, fibi:  %7.6f, percent: %10.2f" % (i, time1, time2, time1 / time2))
