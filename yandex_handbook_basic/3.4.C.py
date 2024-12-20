# Рациональная считалочка
# Напишите программу, которая производит счёт по заданным параметрам.
# Формат ввода
# В одну строку через пробел вводятся 3 рациональных числа — начало счета,
# конец и шаг.
# Формат вывода
# Последовательность чисел с заданными параметрами.
# Пример 1
# Ввод
# 3.2 6.4 0.8
# Вывод
# 3.20
# 4.00
# 4.80
# 5.60
# 6.40
# Пример 2
# Ввод
# 3.14 10 1.57
# Вывод
# 3.14
# 4.71
# 6.28
# 7.85
# 9.42
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt

from itertools import count

start, end, step = map(float, input().split())
for value in count(start, step):
    if value > end:
        break
    print(f"{value:.2f}")

