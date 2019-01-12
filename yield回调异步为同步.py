import random

class IFakeSyncCall(object):
    def __init__(self):
        self.generators = {}

    @staticmethod
    def FAKE_SYNCALL():
        def fwarp(classfunc):
            def fakesyncall(self,*args, **kw):
                self.generators[classfunc.__name__] = classfunc(self, *args, **kw)
                func, args = self.generators[classfunc.__name__].__next__()
                func(*args)
            return fakesyncall
        return fwarp

    def callback_manger(self, funcname, result):
        try:
            func, args = self.generators[funcname].send(result)
            func(*args)
        except:
            self.generators.pop(funcname)


class Server(IFakeSyncCall):
    def __init__(self, palyers):
        super().__init__()
        self.palyers = palyers

    @IFakeSyncCall.FAKE_SYNCALL()
    def count_func(self):
        total = 0
        for palyer in self.palyers:
            id, score = yield (palyer.End, (self, ))
            total += score
            print(total, id)

class Palyer(object):
    def __init__(self, id):
        self.id = id

    def End(self, Handle):
        score = random.randint(1,100)
        Handle.callback_manger("count_func", (self.id, score))


if __name__ == "__main__":
    palys = []
    for i in range(3):
        palys.append(Palyer(i+1))
    server = Server(palys)
    server.count_func()

