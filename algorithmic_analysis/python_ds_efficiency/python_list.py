from timeit import Timer, timeit
# Different ways to create a python list of n numbers starting with 0


def test1():
    list_ = []
    for i in range(1000):
        list_ += [i]

    return list_


def test2():
    list_ = []
    for i in range(1000):
        list_.append(i)

    return list_


def test3():
    list_ = [i for i in range(1000)]

    return list_


def test4():
    return list(range(1000))


# t1 = Timer('test1()', 'from __main__ import test1')
# print('concat performance ', t1.timeit(number=1000), ' ms')

# t2 = Timer('test2()', 'from __main__ import test2')
# print('append performance ', t2.timeit(number=1000), ' ms')

# t3 = Timer('test3()', 'from __main__ import test3')
# print('list comprehension performance ', t3.timeit(number=1000), ' ms')

# t4 = Timer('test4()', 'from __main__ import test4')
# print('list constructor wrapped over range performance ',
#       t4.timeit(number=1000), ' ms')

# from __name__ import test1 means
# import test1 from __name__ namespace into the namespace
# which timeit setups up for the timing experiment.

# Another test to determine if T(n) is O(1) if pop from end of list
# and O(n) if done from beginning of the list

pop_zero = Timer('x.pop(0)', 'from __main__ import x')
pop_end = Timer('x.pop()', 'from __main__ import x')

for i in range(1000000, 100000001, 1000000):
    x = list(range(i))
    pz = pop_zero.timeit(number=1000)

    x = list(range(i))
    pe = pop_end.timeit(number=1000)

    print('{} || {}'.format(pz, pe))
