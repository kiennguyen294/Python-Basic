import timeit
from timeit import Timer


def test_1():
    l = []
    for i in range(1000):
        l = l + [i]


def test_2():
    l = []
    for i in range(1000):
        l.append(i)


def test_3():
    l = [i for i in range(1000)]


def test_4():
    l = list(range(1000))


t1 = Timer("test_1()", "from __main__ import test_1")
print("concat ", t1.timeit(number=1000), "milliseconds")

t2 = Timer("test_2()", "from __main__ import test_2")
print("append ",t2.timeit(number=1000), "milliseconds")

t3 = Timer("test_3()", "from __main__ import test_3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")

t4 = Timer("test_4()", "from __main__ import test_4")
print("list range ",t4.timeit(number=1000), "milliseconds")


popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x.pop(0)", "from __main__ import x")

x = list(range(2000000))
popzero.timeit(number=1000)

x = list(range(2000000))
popend.timeit(number=1000)