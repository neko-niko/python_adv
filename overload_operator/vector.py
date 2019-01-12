from array import array
import reprlib
import math
import itertools
import numbers
import functools
class Vector(object):
    shortcut_names = 'xyzt'
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)


    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['): -1]
        return "Vector({})".format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self._components)))

    def __eq__(self, other):
        return (len(self) == len(other)) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        return functools.reduce(lambda a, b: a^b ,(hash(x) for x in self._components), 0)


    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(self._components[item])
        elif isinstance(item, numbers.Integral):
            return self._components[item]
        else:
            raise TypeError("{.__name__} indices must be integers".format(cls))

    def __setitem__(self, key, value):
        self._components[key] = value

    def __getattr__(self, item):
        cls = type(self)
        if len(item) == 1:
            pos = cls.shortcut_names.find(item)
            if pos >= 0 and pos <= 3:
                return self._components[pos]
        else:
            return AttributeError("{.__name__} object has no attribute".format(cls))



    def __setattr__(self, key, value):
        cls = type(self)
        if len(key) == 1:
            if key in cls.shortcut_names:
                error = 'readonly attribute {attr_name}'
            elif key.islower():
                error = "can't set attribute 'a' to 'z' in {cls_name}"
            else:
                error = ""
            if error:
                raise AttributeError(error.format(attr_name = key, cls_name = cls.__name__))

        super().__setattr__(key, value)



    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(x) for x in range(1, len(self)))

    def __format__(self, format_spec=''):
        if format_spec.endswith('h'):
            coords = itertools.chain([abs(self)], self.angles())
            outer_str = "<{}>"
        else:
            coords = self
            outer_str = "({})"
        componts = (format(c, format_spec[:-1]) for c in coords)
        return outer_str.format(', '.join(componts))



    @classmethod
    def frombytes(cls, octets):
        typecode = octets[0]
        memo = memoryview(octets[1:]).cast(typecode)
        return cls(memo)



if __name__ == "__main__":
    vec = Vector([1, 2, 3, 4])
    print(repr(vec))
    vec.x = 1