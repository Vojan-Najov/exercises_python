# Есть варианты?
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Вася пришёл на образовательный семинар и обнаружил, что зрителей на
# мероприятии — N, а количество мест — M.
# Помогите Васе определить вероятность того, что он попадёт на семинар.
# Формат ввода
# Два числа N и M.
# Формат вывода
# Два числа — количество вариантов, в которых Вася попадает на семинар и
# количество всех вариантов групп на семинаре.
# Примечание
# В первом примере обозначим участников числами 1, 2, 3, 4. Предположим, что
# 1 — это Вася.
# Тогда все вариации участников выглядят так:
#     1 2
#     1 3
#     1 4
#     2 3
#     2 4
#     3 4
# А благополучными из них для Васи являются только 3:
#     1 2
#     1 3
#     1 4
# Пример 1
# Ввод
# 4 2
# Вывод
# 3 6
# Пример 2
# Ввод
# 10 3
# Вывод
# 36 120

from math import comb

n, m = (int(x) for x in input().split())
print(comb(n - 1, m - 1), comb(n, m))
