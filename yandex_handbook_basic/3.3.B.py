# Таблица умножения 2.0
# Вашему решению будет предоставлена единственная переменная n — необходимый
# размер таблицы умножения.
# Напишите списочное выражения для генерации таблицы умножения.
# Примечание
# В решении не должно быть ничего, кроме списочного выражения.
# Пример 1
# Ввод
# n = 3
# Вывод
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
# Пример 2
# Ввод
# n = 4
# Вывод
# [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод

n = int(input().split(" = ")[1])
multtable = [[n1 * n2 for n1 in range(1, n + 1)] for n2 in range(1, n + 1)]
print(multtable)