# Словарная ёлка
# Напишите программу, которая преобразует строку слов в ёлку как показано в
# примере.
# Формат ввода
# В одну строку через пробел вводятся слова разделенные пробелом.
# Формат вывода
# Несколько строк. В каждой следующей строке на одно слово больше.
# Примечание
# accumulate «складывает» не только числа.
# Пример 1
# Ввод
# мама мыла раму
# Вывод
# мама
# мама мыла
# мама мыла раму
# Пример 2
# Ввод
# картина корзина картонка
# Вывод
# картина
# картина корзина
# картина корзина картонка
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt

from itertools import accumulate

for val in accumulate([w] for w in input().split()):
    print(" ".join(val))