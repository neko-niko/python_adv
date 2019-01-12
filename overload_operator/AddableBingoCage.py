from abstract_base_class.MyABC import BingoCage

class AddableBingoCage(BingoCage):
    def __add__(self, other):
        if isinstance(other, BingoCage.__mro__[1]):
            BingoCage1 = self.inspect()
            BingoCage2 = other.inspect()
            return AddableBingoCage(BingoCage1 + BingoCage2)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, BingoCage):
            other_iterable = other.inspect()

        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                raise TypeError(self_cls)
        self.load(other_iterable)
        return self

