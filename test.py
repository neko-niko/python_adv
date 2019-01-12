# class X(object):
#     pass
#
# def __evil_eq__(self, other):
#     print ('hello world')
#     return False
#
# def evil(y):
#     d = {X(): 1}
#     X.__eq__ = __evil_eq__
#     d[y] # might trigger a call to __eq__?
# import
class StrKeyDict(dict):
    def get(self, key):
        try:
            return super().get(key)
        except:
            raise KeyError()

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError()
        return self[str(key)]


class Test1(object):
    def __init__(self):
        super().__init__()

    def f(self, x):
        print(x)

def test_conr():
    lst = []
    while True:
        x = yield
        if x == None:
            break

        lst.append(x)

    return lst


def grouper(dct):
    cot = 0
    while True:
        dct[cot] = yield from test_conr()
        cot += 1



if __name__ == "__main__":
    import requests

    res = requests.get("http://127.0.0.1:8000/test1/lgzp/1")
    print(res.text)
# def grouper(lst):
