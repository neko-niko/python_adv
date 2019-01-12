#本质将非字符串转化为字符串

class StrKetDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        else:
            return self[str(key)]

    def get(self, key, default = None):
        try:
            return self[key]
        except:
            return default

    def __contains__(self, item):
        return item in self.keys() or str(item) in self.keys()
