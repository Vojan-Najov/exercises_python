# Кашееды — 4
# Каждый воспитанник детского сада любит одну или несколько каш.
# Поможем воспитателю составить список детей, которые любят конкретную кашу.
# Формат ввода
# В первой строке задаётся количество детей в группе (N). В следующих N строках
# записана фамилия ребенка и список его любимых каш. В последней строке
# записана каша, информацию о которой хочет получить воспитатель.
# Формат вывода
# Фамилии учеников, которые любят заданную кашу, в алфавитном порядке.
# Если таких не окажется, в строке вывода нужно написать «Таких нет».
# Пример 1
# Ввод
# 5
# Васильев манная
# Петров манная
# Васечкин манная
# Иванов овсяная
# Михайлов овсяная
# манная
# Вывод
# Васечкин
# Васильев
# Петров
# Пример 2
# Ввод
# 3
# Иванов манная овсяная
# Петров манная овсяная
# Васечкин манная овсяная
# гречневая
# Вывод
# Таких нет
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt

n = int(input())
porriges = {}
for _ in range(n):
    name, *prgs = input().split()
    for prg in prgs:
        porriges[prg] = porriges.get(prg, []) + [name]

porrige = input()
print("\n".join(sorted(porriges[porrige])) if porrige in porriges else "Таких нет")
