# Хвост
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# В семействе операционных систем Linux существует одна прекрасная консольная
# утилита — tail. Она предназначена для случаев, когда нам не нужно читать
# весь файл, а достаточно просмотреть только несколько последних строк.
# Напишите аналог этой утилиты.
# Формат ввода
# Пользователь вводит имя файла (F), а затем количество строк (N), которые он
# хочет увидеть.
# Формат вывода
# Выведите N последних строк файла F.
# Пример
# Ввод
# # Пользовательский ввод:
# some_file.txt
# 2
# # Содержимое файла some_file.txt
# 1 строка
# 2 строка
# 3 строка
# 4 строка
# 5 строка
# Вывод
# 4 строка
# 5 строка

from sys import stdout

filename = input()
n = int(input())

with open(filename) as f:
    lines = f.readlines()
    if n > 0:
        stdout.writelines(lines[-n:])

