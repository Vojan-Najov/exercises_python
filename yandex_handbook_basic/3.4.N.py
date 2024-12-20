# Спортивные гадания
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt
# Хорошо, спортсмены расставлены на старте. Вот только угадать финалистов
# практически невозможно. Давайте напишем программу, которая выводит список
# возможных победителей.
# Формат ввода
# В первой строке задано натуральное число N — количество спортсменов. В
# следующих N строках записаны имена спортсменов.
# Формат вывода
# Отсортированный по алфавиту список вариантов.
# Имена в каждой строке выводить через запятую и пробел.
# Пример 1
# Ввод
# 3
# Аня
# Боря
# Вова
# Вывод
# Аня, Боря, Вова
# Аня, Вова, Боря
# Боря, Аня, Вова
# Боря, Вова, Аня
# Вова, Аня, Боря
# Вова, Боря, Аня
# Пример 2
# Ввод
# 4
# Вова
# Аня
# Дима
# Боря
# Вывод
# Аня, Боря, Вова
# Аня, Боря, Дима
# Аня, Вова, Боря
# Аня, Вова, Дима
# Аня, Дима, Боря
# Аня, Дима, Вова
# Боря, Аня, Вова
# Боря, Аня, Дима
# Боря, Вова, Аня
# Боря, Вова, Дима
# Боря, Дима, Аня
# Боря, Дима, Вова
# Вова, Аня, Боря
# Вова, Аня, Дима
# Вова, Боря, Аня
# Вова, Боря, Дима
# Вова, Дима, Аня
# Вова, Дима, Боря
# Дима, Аня, Боря
# Дима, Аня, Вова
# Дима, Боря, Аня
# Дима, Боря, Вова
# Дима, Вова, Аня
# Дима, Вова, Боря

from itertools import permutations

for perm in permutations(sorted(input() for _ in range(int(input()))), 3):
    print(*perm, sep=", ")
