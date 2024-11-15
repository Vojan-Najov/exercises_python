# Игровая сетка
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt
# Ребята в классе решили устроить чемпионат по шашкам. К сожалению, количество
# учеников не является степенью двойки и поэтому классическую турнирную сетку
# создать сложно. Для выявления фаворитов ребята договорились сыграть по
# принципу «каждый с каждым». Продумайте программу, которая составляет список
# необходимых игр.
# Формат ввода
# В первой строке записано число учеников (N).
# В каждой из последующих N строк записано одно имя.
# Формат вывода
# Список игр в формате:
# <Игрок 1> - <Игрок 2>
# Порядок игр не имеет значения.
# Пример
# Ввод
# 3
# Аня
# Боря
# Вова
# Вывод
# Аня - Боря
# Аня - Вова
# Боря - Вова

from itertools import combinations

participants = (input() for _ in range(int(input())))
for p1, p2 in combinations(participants, 2):
    print(f"{p1} - {p2}")
