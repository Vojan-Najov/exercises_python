# RLE наоборот
# Вашему решению будет предоставлен список кортежей rle с символами и
# количеством их повторений.
# Напишите выражение для генерации строки, из которой был получен данный список.
# Примечание
# В решении не должно быть ничего, кроме выражения.
# Пример 1
# Ввод
# rle = [('a', 2), ('b', 3), ('c', 1)]
# Вывод
# 'aabbbc'
# Пример 2
# Ввод
# rle = [('1', 1), ('0', 2), ('5', 1), ('0', 2)]
# Вывод
# '100500'
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод

exec(input())
s = "".join(smb for smb, n in rle for i in range(n))
print(s)
