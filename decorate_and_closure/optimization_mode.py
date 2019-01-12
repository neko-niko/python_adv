promo_lst = []
def promo_regis(func):
    promo_lst.append(func)
    return func

@promo_regis
def fidelity_promo(order):
    if order.customer.fidelity >= 1000:
        return order.total()*0.1

@promo_regis
def buliitem_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount

@promo_regis
def largeorder_promo(order):
    if len(set(product.product for product in order.cart)) >= 10:
        return order.total() * 0.07
    return 0
