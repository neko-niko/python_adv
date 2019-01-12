import collections

class DoppelDict(dict):         #直接继承子类
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


class DopplDict2(collections.UserDict):          #继承用户定制子类
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


if __name__ == "__main__":
    dd = DopplDict2(one = 1)
    print(dd)
    dd['two'] = 2
    print(dd)
    dd.update(there = 3)
    print(dd)
