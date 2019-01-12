from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', ['name', 'fidelity'])
#经典策略模式
class LineItem:     #顾客商品
    def __init__(self, product, quantity, price):
        self.product = product      #名称
        self.quantity = quantity    #数量
        self.price = price          #价格

    def total(self):
        return self.price*self.quantity


class Order:
    def __init__(self, customer, cart, promotion = None):
        self.customer = customer    #顾客
        self.cart = list(cart)      #购物车
        self.promotion = promotion      #折扣

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)

        return self.__total

    def due(self):
        if self.promotion == None:
            discount = 0
        else:
            discount = self.promotion.discount(self)

        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total:{:.2f} due:{:.2f}'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        pass

class FidelityPromo(Promotion):
    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion):
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount

class LargeOrderPromo(Promotion):
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0


#使用函数实现，不需要定义抽象类与其实现

def fidelity_promo(order):
    if order.customer.fidelity >= 1000:
        return order.total()*0.1

def buliitem_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount
def largeorder_promo(order):
    if len(set(product.product for product in order.cart)) >= 10:
        return order.total() * 0.07
    return 0

#使用单独模块
from mode import promo
import inspect
promo_lst = [func for name, func in inspect.getmembers(promo)]
def best_promo(order):
    return max(discount(order) for discount in promo_lst)


import functools
def lines(a, b, x):
    return a * x + b

def out_func(a, b):
    def dec_func(func):
        def wapper(x):
            return func(a, b, x)
        return wapper
    return dec_func

if __name__ == "__main__":
    one_one_lines = functools.partial(lines, 1, 1)
    print(one_one_lines(1))
