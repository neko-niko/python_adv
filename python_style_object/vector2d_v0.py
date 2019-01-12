from array import array
import math
class Vector2d(object):
    typecode = 'd'
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x ,self.y))

    def __repr__(self):
        return "{}({!r}, {!r})".format(self.__class__.__name__, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, format_spec=''):       #自定义format
        if format_spec.endswith('p'):
            coords = (abs(self), self.angle())
            outer = "<{}, {}>"
        else:
            coords = self
            outer = "({}, {})"
        coords = (format(c, format_spec[:-1]) for c in coords)
        return outer.format(*coords)

    def __hash__(self):
        return hash(self.x)^hash(self.y)


    def angle(self):
        return math.atan2(self.y, self.x)


    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return (cls(*memv))



if __name__ == "__main__":
    vec = Vector2d(3, 4)
    print(bytes(vec))
    for i in bytes(vec):
        print(i)
