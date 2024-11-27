# "Выпрямление" списка
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Весьма часто, данные, которые мы получаем из различных источников, не
# удовлетворяют нашим пожеланиям. Одна из частых проблем – излишняя
# вложенность списков.
# Напишите функцию make_linear, которая принимает список списков и возвращает
# его "выпрямленное" представление.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций, за исключением рекурсивных.
# Трассировка вызова рекурсивной функции в обработке ответа не учитывается и
# показана для примера.
# Пример 1
# Ввод
# result = make_linear([1, 2, [3]])
# Вывод
# # Вызов make_linear([1, 2, [3]])
# # Вызов make_linear([3])
# result = [1, 2, 3]
# Пример 2
# Ввод
# result = make_linear([1, [2, [3, 4]], 5, 6])
# Вывод
# # Вызов make_linear([1, [2, [3, 4]], 5, 6])
# # Вызов make_linear([2, [3, 4]])
# # Вызов make_linear([3, 4])
# result = [1, 2, 3, 4, 5, 6]

def make_linear(alist):
    # print(f'make_linear({alist})')
    res = []
    for item in alist:
        if isinstance(item, list):
            res.extend(make_linear(item))
        else:
            res.append(item)
    return res

            
if __name__ == '__main__':
    result = make_linear([1, 2, [3]])
    assert result == [1, 2, 3]

    result = make_linear([1, [2, [3, 4]], 5, 6])
    assert result == [1, 2, 3, 4, 5, 6]