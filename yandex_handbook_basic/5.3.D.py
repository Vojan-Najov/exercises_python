# Контроль параметров
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Напишите функцию only_positive_even_sum, которая принимает два параметра и
# возвращает их сумму.
# Если один из параметров не является целым числом, то следует вызвать
# исключение TypeError.
# Если один из параметров не является положительным чётным числом, то следует
# вызвать исключение ValueError.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# print(only_positive_even_sum("3", 2.5))
# Вывод
# Вызвано исключение TypeError
# Пример 2
# Ввод
# print(only_positive_even_sum(-5, 4))
# Вывод
# Вызвано исключение ValueError

def only_positive_even_sum(a, b):
    if not isinstance(a, int) and not isinstance(b, int):
        raise TypeError()
    if a < 0 or a % 2 or b < 0 or b % 2:
        raise ValueError()
    return a + b

try:
    print(only_positive_even_sum("3", 2.5))
except Exception as e:
    print(type(e))

try:
    print(only_positive_even_sum(-5, 4))
except Exception as e:
    print(type(e))

print(only_positive_even_sum(10, 4))

