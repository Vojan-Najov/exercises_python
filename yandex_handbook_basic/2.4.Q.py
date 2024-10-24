# А роза упала на лапу Азора 3.0
# Вернёмся к палиндромам. Напишите программу, которая определяет количество
# палиндромов в переданном списке.
# Формат ввода
# В первой строке записано число NN Во всех последующих NN строках указано по
# одному числу.
# Формат вывода
# Требуется вывести общее количество палиндромов среди введённых чисел
# (кроме числа NN).
# Пример 1
# Ввод
# 5
# 1
# 2
# 3
# 4
# 5
# Вывод
# 5
# Пример 2
# Ввод
# 3
# 123
# 454
# 321
# Вывод
# 1
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt

nn = int(input())
count = 0

for i in range(nn):
    num = int(input())
    tmp = num
    rev = 0

    while tmp:
        rev *= 10
        rev += tmp % 10
        tmp //= 10

    if rev == num:
        count += 1

print(count)
