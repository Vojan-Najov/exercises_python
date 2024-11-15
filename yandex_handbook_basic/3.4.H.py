# Меню питания 2.0
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt
# В детском саду ежедневно подают новую кашу на завтрак.
# Напишите программу, которая строит расписание каш на ближайшие дни.
# Формат ввода
# Вводится натуральное число M — количество каш в меню. В каждой из последующих
# M строк записано одно название каши. В конце передается натуральное число N —
# количество дней.
# Формат вывода
# Вывести список каш в порядке подачи.
# Примечание
# Советуем изучить документацию на функцию itertools.islice, которая реализует
# срезы на основе итераторов.
# Пример 1
# Ввод
# 5
# Манная
# Гречневая
# Пшённая
# Овсяная
# Рисовая
# 3
# Вывод
# Манная
# Гречневая
# Пшённая
# Пример 2
# Ввод
# 5
# Манная
# Гречневая
# Пшённая
# Овсяная
# Рисовая
# 12
# Вывод
# Манная
# Гречневая
# Пшённая
# Овсяная
# Рисовая
# Манная
# Гречневая
# Пшённая
# Овсяная
# Рисовая
# Манная
# Гречневая

from itertools import islice, cycle

porriges = [input() for _ in range(int(input()))]
for porrige in islice(cycle(porriges), int(input())):
    print(porrige)