# Потоковый НОД
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Напишите программу, находящую наибольшие общие делители для всех переданных
# в стандартный поток последовательностей чисел.
# Формат ввода
# Вводятся строки чисел, разделённых пробелами.
# Формат вывода
# Последовательность чисел — наибольшие общие делители всех последовательностей.
# Пример
# Ввод
# 2 1000 20 34
# 36 12
# 3 96 12
# 6
# 7 8 9 10
# Вывод
# 2
# 12
# 3
# 6
# 1

from sys import stdin
import math


while s := stdin.readline():
    print(math.gcd(*[int(word) for word in s.split()]))
