import weakref
class cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(self):
        return "Cheese(%r)" % self.kind


stock = weakref.WeakValueDictionary()     #弱引用映射,不改变引用计数
catalog = [cheese("Red Lecicester"), cheese("Tilsit"), cheese("Brie"), cheese("Parmesan")]


for Cheese in catalog:
    stock[Cheese.kind] = Cheese
print(stock.__dict__)
print(sorted(stock.keys()))
del catalog
print(list(stock.keys()))
del Cheese         #删除临时引用
print(list(stock.keys()))
