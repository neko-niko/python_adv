import functools
def singledispatch(func):
    class Dispatch(object):
        def __init__(self):
            self.map = {}
            self.map['base'] = func

        def register(self, param):
            def decorator(dispatch_func):
                self.map[param] = dispatch_func
                return dispatch_func
            return decorator

        def __call__(self, param):
            instance = functools.partial(isinstance, type(param))
            type_dict = {instance(item):func for item, func in self.map.items() if item != 'base'}
            if any(type_dict.keys()):
                func2 = type_dict[True]
            else:
                func2 = self.map['base']
            return func2(param)
    return Dispatch()
