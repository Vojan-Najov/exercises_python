# Акция
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Магазин, для которого вы писали функцию в предыдущей задаче, проводит акцию:
# При покупке больше двух товаров — скидка 50%
# мелкий шрифт: скидка распространяется только на товары купленные в количестве
# более двух штук
# Напишите функцию discount, принимающую чек из прошлой задачи и возвращающую
# новый с учётом акции.
# Примечание
# Не удаляйте функцию cheque, она потребуется для тестирования.
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Пример
# Ввод
# products = ['bread', 'milk', 'soda', 'cream']
# prices = [37, 58, 99, 72]
# price_list = pd.Series(prices, products)
# result = cheque(price_list, soda=3, milk=2, cream=1)
# with_discount = discount(result)
# print(result)
# print(with_discount)
# Вывод
#   product  price  number  cost
# 0   cream     72       1    72
# 1    milk     58       2   116
# 2    soda     99       3   297
#   product  price  number   cost
# 0   cream     72       1   72.0
# 1    milk     58       2  116.0
# 2    soda     99       3  148.5

import pandas as pd


def cheque(price_list, **kwargs):
    d = {}
    keys = list(sorted(kwargs.keys()))
    d['product'] = keys
    d['price'] = [price_list[k] for k in keys]
    d['number'] = [kwargs[k] for k in keys]
    d['cost'] = [d['number'][i] * d['price'][i] for i, _ in enumerate(keys)]

    return pd.DataFrame(d)


def discount(cheque):
    dsc = cheque[['product', 'price', 'number']]
    dsc['cost'] = [
        cost / 2 if cheque['number'][i] > 2 else cost
        for i, cost in enumerate(cheque['cost'])
    ]
    return dsc

def main():
    products = ['bread', 'milk', 'soda', 'cream']
    prices = [37, 58, 99, 72]
    price_list = pd.Series(prices, products)
    result = cheque(price_list, soda=3, milk=2, cream=1)
    with_discount = discount(result)
    print(result)
    print(with_discount)


if __name__ == '__main__':
    main()


