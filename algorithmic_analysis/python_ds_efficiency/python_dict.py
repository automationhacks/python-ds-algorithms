import random
from timeit import Timer, timeit

for i in range(10000, 1000000, 20000):
    # take a random no within range to
    # check if it is contained.
    
    test = Timer(
        'random.randrange(%d) in x' % i,
        'from __main__ import random, x'
        )

    # make a list
    x = list(range(i)) 
    list_time = test.timeit(number=1000)

    # make a dict
    x = {k: None for k in range(i)}
    dict_time = test.timeit(number=1000)

    print('%d, %10.3f, %10.3f' % (i, list_time, dict_time))
