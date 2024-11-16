# Таблица истинности 2
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt
# Продолжим работу с таблицами истинности. Продумайте программу, которая для
# введённого сложного логического высказывания строит таблицу истинности.
# Формат ввода
# Вводится логическое выражение от нескольких переменных валидное для языка
# Python.
# Формат вывода
# Выведите таблицу истинности данного выражения.
# Примечание
# В выражении все переменные заданы заглавными латинскими буквами.
# Обратите внимание на параметры __globals и __locals у функции eval.
# Пример 1
# Ввод
# not A or B and C
# Вывод
# A B C F
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
# A and not B and A
# Вывод
# A B F
# 0 0 0
# 0 1 0
# 1 0 1
# 1 1 0

from itertools import product

expr = input()
logvars = filter(lambda x: x not in ("and", "or", "not"), expr.split())
logvars = list(sorted({x for x in logvars}))
print(" ".join(logvars + ['F']))

it = product((0, 1), repeat=len(logvars))
for comb in it:
    f = int(eval(expr, {x: y for x, y in zip(logvars, comb)}))
    print(" ".join(map(str, list(comb) + [f])))

