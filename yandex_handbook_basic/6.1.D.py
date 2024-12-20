# Среднее не арифметическое
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Средним геометрическим нескольких положительных вещественных чисел называют
# такое число, которым можно заменить каждое из этих чисел так, чтобы их
# произведение не изменилось.
# Формула среднего геометрического для n n чисел выглядит так:
# G(x1, x2, ..., xn ) = (x1 ⋅ x2 ⋅⋅⋅ xn)^1/n 
# Формат ввода
# Вводится последовательность рациональных чисел, разделённых пробелами.
# Формат вывода
# Одно число — среднее геометрическое переданных чисел.
# Пример 1
# Ввод
# 1 2 3 4 5
# Вывод
# 2.605171084697352
# Пример 2
# Ввод
# 1.1 1.2 1.3 1.4 1.5
# Вывод
# 1.292252305460076

from math import prod, pow

nums = [float(x) for x in input().split()]
print(pow(prod(nums), 1 / len(nums)))

