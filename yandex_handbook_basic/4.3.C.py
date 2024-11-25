# Многочлен N-ой степени
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Напишите функцию make_equation, которая по заданным коэффициентам строит
# строку, описывающую валидное с точки зрения Python выражение без
# использования оператора возведения в степень.
# Многочлен второй степени с коэффициентами a, b и c, например, можно записать
# в виде:
# ((a)∗x+b)∗x+c
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций, за исключением рекурсивных.
# Трассировка вызова рекурсивной функции в обработке ответа не учитывается и
# показана для примера.
# Пример 1
# Ввод
# result = make_equation(3, 2, 1)
# Вывод
# # Вызов make_equation(3, 2, 1)
# # Вызов make_equation(3, 2)
# # Вызов make_equation(3)
# result = '((3) * x + 2) * x + 1'
# Пример 2
# Ввод
# result = make_equation(3, 1, 5, 3)
# Вывод
# # Вызов make_equation(3, 1, 5, 3)
# # Вызов make_equation(3, 1, 5)
# # Вызов make_equation(3, 1)
# # Вызов make_equation(3)
# result = '(((3) * x + 1) * x + 5) * x + 3'

def make_equation(*args):
    if len(args) == 1:
        return str(args[0])
    return '(' + make_equation(*args[:-1]) + f') * x + {args[-1]}'


if __name__ == '__main__':
    assert make_equation(3, 2, 1) == '((3) * x + 2) * x + 1'
    assert make_equation(3, 1, 5, 3) == '(((3) * x + 1) * x + 5) * x + 3'