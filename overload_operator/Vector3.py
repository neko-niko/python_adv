from overload_operator.vector import Vector
import math
import decimal
from collections import Counter
import random
import itertools
import numbers



class Vector_v3(Vector):
    def __init__(self, array):
        super().__init__(array)


    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __neg__(self):
        return Vector_v3(-x for x in self)

    def __pos__(self):
        return Vector_v3(self)

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)       #zip两个可迭代类型，并为短的填0
            return Vector(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented       #如果报错 返回NotImplemented 尝试调用反向运算符


    def __radd__(self, other):
        return self + other


    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return Vector_v3(x * other for x in self)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (len(self)  == len(other) and all(a == b for a, b in zip(self, other)))
        else:
            return NotImplemented


if __name__ == "__main__":
    pass

