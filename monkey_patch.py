saved = {}

def patch_item(module, attr, newitem):
    NODE = object()
    olditem = getattr(module, attr, NODE)
    if olditem is not NODE:
        saved.setdefault(module.__name__, {}).setdefault(attr, olditem)
    setattr(module, attr, newitem)

def patch_module(name, items=None):
    gevent_module = getattr(__import__("gevent." + name), name)     #获取用于做补丁的模块
    module_name = getattr(gevent_module, "__target__", name)        #用于做补丁的模块中含有被补丁的模块的默认名，如果没有则为传入的name
    module = __import__(module_name)            #获取要打补丁的模块
    if items is None:
        items = getattr(gevent_module, "__implements__", None)      #如果作为替换的具体属性为空，则从补丁模块中获取用于补丁的默认名
        if items is None:
            raise AttributeError("%s not have __implements__" % gevent_module)

    for attr in items:
        patch_item(module, attr, getattr(gevent_module, attr))




