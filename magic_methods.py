from math import hypot,sqrt


class Vector(object):
    def __init__(self, x, y):
        self.x_ = x
        self.y_ = y

    def __repr__(self):
        return self.__class__.__name__ + "(%s,%s)" % (self.x_, self.y_)

    def __abs__(self):
        return hypot(self.x_, self.y_)

    def __add__(self,other):
        if other.__class__ != self.__class__:
         raise ValueError("object %s can't add object %s" % (self.__class__.__name__, other.__class__.__name__))
        else:
         return Vector(self.x_ + other.x_ , self.y_ + other.y_)

    def __bool__(self):
        return bool(self.x_ or self.y_)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x_ * other, self.y_ * other)
        elif self.__class__ == other.__class__:
            return sqrt(self.x_ * other.x_ + self.y_ * other.y_)
        else:
            raise ValueError("object %s can't mul object %s" % (other.__class__.__name__, self.__class__.__name__))

if __name__ == "__main__":
    v = Vector(3, 4)
    print(v.__class__)
    print(type(v))