# Мы делили апельсин 2.0
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt
# Аня, Боря и Вова решили съесть апельсин.
# Подскажите ребятам, как им его разделить.
# Разработайте программу, которая выводит все возможные способы разделки
# апельсина.
# Формат ввода
# В единственной строке записано количество долек апельсина (N).
# Формат вывода
# Таблица вариантов разделения апельсина.
# Примечания
#     Каждому ребёнку должна достаться хотя бы одна долька апельсина.
#     Ни одной дольки не должно остаться.
#     Выводить варианты в порядке увеличения количества долек у Ани,
#     следом Бори и затем Вовы.
# Для удобства сведите задачу к разделению долек между двумя ребятами, а
# третьему отдайте остатки.
# Пример 1
# Ввод
# 3
# Вывод
# А Б В
# 1 1 1
# Пример 2
# Ввод
# 5
# Вывод
# А Б В
# 1 1 3
# 1 2 2
# 1 3 1
# 2 1 2
# 2 2 1
# 3 1 1

from itertools import product

n = int(input())

print("А", "Б", "В")
for p1, p2 in product(range(1, n - 1), repeat=2):
    if p1 + p2 < n:
        print(p1, p2, n - p1 - p2)

