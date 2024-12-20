# Файловая разница
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Напишите программу, которая определяет, какие слова есть только в одном из
# файлов.
# Формат ввода
# Пользователь вводит три имени файлов.
# Каждый из входных файлов содержит произвольное количество слов, разделённых
# пробелами и символами перевода строки.
# Формат вывода
# В третий файл выведите в алфавитном порядке без повторений список слов,
# которые есть только в одном из файлов.
# Пример
# Ввод
# # Пользовательский ввод:
# first.txt
# second.txt
# answer.txt
# # Содержимое файла first.txt
# кофе молоко
# чай печенье
# велосипед
# # Содержимое файла second.txt
# кофе велосипед
# пряник жвачка весло
# Вывод
# # Содержимое файла answer.txt
# весло
# жвачка
# молоко
# печенье
# пряник
# чай

infilename1, infilename2, outfilename = input(), input(), input()

s1 = set()
with open(infilename1, "r") as in1:
    for line in in1:
        for word in line.split():
            s1.add(word)

s2 = set()
with open(infilename2, "r") as in2:
    for line in in2:
        for word in line.split():
            s2.add(word)

s = s1.symmetric_difference(s2)
with open(outfilename, "w") as out:
    for word in sorted(s):
        print(word, file=out)

