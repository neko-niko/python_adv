import abc
import random
import doctest
import collections

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        '''从可迭代对象中添加元素'''

    @abc.abstractmethod
    def pick(self):
        '''删除随机元素后将删除的元素返回'''
        '''如果为空，则抛出LookupError'''

    def loaded(self):
        '''如果为空 返回False，否则返回True'''
        return bool(self.inspect())

    def inspect(self):
        '''返回一个有序元祖，表示当前的元素'''
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))



class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, iterable):
        self._items.extend(iterable)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty BingoCage")

    def __call__(self):
        self.pick()

class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except:
            raise LookupError("pick from empty LotteryBlower")
        return self._balls[position]

    def load(self, iter):
        self._balls.extend(iter)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(self._balls)


@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            postition = random.randrange(len(self))
            return self.pop(postition)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))





if __name__ == "__main__":
    test = BingoCage([1, 2, 3, 4])
    for _ in range(4):
        print(test.pick())

    print(test.inspect())
    print(test.loaded())