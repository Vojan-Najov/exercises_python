# Частная собственность
# Ребята приносят игрушки в детский сад и играют все вместе.
# Сегодня они решили выяснить, игрушки какого типа принадлежат только одному из
# детей. Напишите программу, которая по списку детей и их игрушек определит
# «частную собственность».
# Формат ввода
# В первой строке задается количество детей в группе (N).
# В каждой из следующих N строк записано имя ребенка и его игрушки в формате:
# Имя: игрушка1, игрушка2, ....
# Формат вывода
# Список игрушек, которые есть только у одного из детей в алфавитном порядке.
# Пример
# Ввод
# 3
# Аня: кукла, машинка, кукла, домик
# Боря: машинка, зайчик
# Вова: кубики, машинка
# Вывод
# домик
# зайчик
# кубики
# кукла
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt

toys = {}
for _ in range(int(input())):
    for toy in set(input().split(":")[1].strip().split(", ")):
        toys[toy] = toys.get(toy, 0) + 1

print("\n".join(sorted([toy for toy in toys if toys[toy] == 1])))