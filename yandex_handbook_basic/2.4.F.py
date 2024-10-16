# НОД 2.0
# В одном из местных НИИ часто требуется находить наибольший общий делитель
# (НОД) нескольких чисел. Вам уже доверяют, так что вновь пришли с этой
# задачей.
# Формат ввода
# В первой строке записано одно число NN — количество данных. В каждой из
# последующих NN строк записано по одному натуральному числу.
# Формат вывода
# Требуется вывести одно натуральное число — НОД всех данных чисел (кроме NN).
# Примечание
# Самый распространённый способ поиска НОД — Алгоритм Евклида.
# Пример 1
# Ввод
# 2
# 12
# 42
# Вывод
# 6
# Пример 2
# Ввод
# 3
# 102
# 39
# 768
# Вывод
# 3
# 
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt

nn = int(input())
nod = int(input())
nn -= 1
while nn > 0:
    n = int(input())
    m = nod
    while m:
        n, m = m, n % m
    nod = n
    nn -= 1

print(nod)