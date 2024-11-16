# Таблица истинности
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt
# Вся современная электронно-вычислительная техника строится на Булевой
# алгебре, которая оперирует истинностью и ложностью высказываний. Любой язык
# программирования содержит логические операции (в Python это and, or, not).
# Чаще всего для работы со сложными высказываниями прибегают к методу под
# названием «Таблица истинности».
# Суть метода проста — рассматриваются все возможные значения входных
# переменных и для них вычисляется результат.
# Разработайте программу, которая для введённого сложного логического
# высказывания строит таблицу истинности.
# Формат ввода
# Вводится логическое выражение от трех переменных (a, b, c) валидное для
# языка Python.
# Формат вывода
# Выведите таблицу истинности данного выражения.
# Примечание
# Для выполнения Python кода, записанного в строках, существуют две
# замечательные функции: exec и eval.
# Пример 1
# Ввод
# not a or b and c
# Вывод
# a b c f
# 0 0 0 1
# 0 0 1 1
# 0 1 0 1
# 0 1 1 1
# 1 0 0 0
# 1 0 1 0
# 1 1 0 0
# 1 1 1 1
# Пример 2
# Ввод
# a and not b and c
# Вывод
# a b c f
# 0 0 0 0
# 0 0 1 0
# 0 1 0 0
# 0 1 1 0
# 1 0 0 0
# 1 0 1 1
# 1 1 0 0
# 1 1 1 0

from itertools import product

expr = input()
print("a b c f")
it = product((0, 1), repeat=3)
for a, b, c in it:
    f = int(eval(expr))
    print(a, b, c, f)
