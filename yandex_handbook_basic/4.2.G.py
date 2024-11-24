# В эфире рубрика «Эксперименты»
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Лаборанты проводят эксперимент и запросили разработку системы обработки данных.
# Результатами эксперимента должны стать пары рациональных чисел.
# Для работы им требуются функции:
#     enter_results(first, second, ...) — добавление данных одного или
#                                         нескольких результатов (гарантируется,
#                                         что количество параметров будет чётным);
#     get_sum() — возвращает пару сумм результатов экспериментов;
#     get_average() — возвращает пару средних арифметических значений
#                     результатов экспериментов.
# Все вычисления производятся с точностью до сотых.
# Примечание
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# enter_results(1, 2, 3, 4, 5, 6)
# print(get_sum(), get_average())
# enter_results(1, 2)
# print(get_sum(), get_average())
# Вывод
# (9, 12) (3.0, 4.0)
# (10, 14) (2.5, 3.5)
# Пример 2
# Ввод
# enter_results(3.5, 2.14, 45.2, 37.99)
# print(get_sum(), get_average())
# enter_results(5.2, 7.3)
# print(get_sum(), get_average())
# enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
# print(get_sum(), get_average())
# Вывод
# (48.7, 40.13) (24.35, 20.07)
# (53.9, 47.43) (17.97, 15.81)
# (58.27, 54.7) (9.71, 9.12)

def enter_results(*args):
    global _results
    if '_results' not in globals():
        _results = {'sum1': 0, 'sum2': 0, 'len1': 0, 'len2': 0}

    for i, res in enumerate(args):
        if i % 2 == 0:
            _results['sum1'] += res
            _results['len1'] += 1
        else:
            _results['sum2'] += res
            _results['len2'] += 1
    _results['avg1'] = _results['sum1'] / _results['len1']
    _results['avg2'] = _results['sum2'] / _results['len2']


def get_sum():
    global _results
    return round(_results.get('sum1', 0), 2), round(_results.get('sum2', 0), 2)


def get_average():
    global _results
    return round(_results.get('avg1', 0), 2), round(_results.get('avg2', 0), 2)


if __name__ == '__main__': 
    enter_results(1, 2, 3, 4, 5, 6)
    print(get_sum(), get_average())
    enter_results(1, 2)
    print(get_sum(), get_average())

    print()
    del _results
    enter_results(3.5, 2.14, 45.2, 37.99)
    print(get_sum(), get_average())
    enter_results(5.2, 7.3)
    print(get_sum(), get_average())
    enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
    print(get_sum(), get_average())
