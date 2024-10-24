# Азбука
# Знакомые нам воспитанники детского сада наконец-то начали учить буквы.
# Воспитатель предложил ребятам назвать слова, которые начинаются с А, Б или В.
# Напишите программу, которая проверяет, что первая буква во всех словах —
# А, Б или В.
# Формат ввода
# Вводится натуральное число NN — количество слов, названных детьми.
# В каждой из последующих NN строк записано по одному слову строчными буквам.
# Формат вывода
# YES — если все слова начинаются с нужной буквы.
# NO — если хотя бы одно слово начинается не с нужной буквы.
# Пример 1
# Ввод
# 3
# арбуз
# барабан
# ворона
# Вывод
# YES
# Пример 2
# Ввод
# 4
# аист
# вареник
# кузнечик
# алыча
# Вывод
# NO
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt

nn = int(input())

for _ in range(nn):
    word = input()
    if word[0].upper() not in ['А', 'Б', 'В']:
        print("NO")
        break
else:
    print("YES")
