import random
import time
import functools


def averager():
    total = 0
    count = 0
    avg = None
    while True:
        x = yield avg
        if x == None:
            break
        count += 1
        total += x
        avg = total / count
    return (count, avg)


def Grouper(results, key):
    while True:
        results[key] = yield from averager()



def main(data):
    results = {}
    # print(data)
    # print(results)
    for key,values in data.items():
        group = Grouper(results, key)
        group.__next__()
        for value in values:
            step_avg = group.send(value)
            print(step_avg)
        group.send(None)

    print(results)

def test(*args):
    for i in args:
        x = yield from i
        print(x)

if __name__ == "__main__":
    # data = {"test1":[1,2,4,5,6], "test2":[3,4,5,6,8]}
    # # print(data)
    # main(data)
    test1 = test('acv','ddf')
    for i in range(6):
        print(test1.__next__())




        