# Длины всех слов
# Вашему решению будет предоставлена строка sentence слов, разделённых
# пробелами.
# Напишите списочное выражения для генерации списка длин слов.
# Примечание
# В решении не должно быть ничего, кроме списочного выражения.
# Пример 1
# Ввод
# sentence = 'Мама мыла раму'
# Вывод
# [4, 4, 4]
# Пример 2
# Ввод
# sentence = 'Ехали медведи на велосипеде'
# Вывод
# [5, 7, 2, 10]
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод

sentence = input()
lens = [len(word) for word in sentence.split()]
print(lens)
