# Кашееды — 2
# Изменим задачу и напишем программу, которая поможет быстро выяснить, сколько
# детей любят только одну кашу.
# Формат ввода
# В первых двух строках указывается количество детей, любящих манную и овсяную
# каши (N и M).
# Затем идут N + M строк — перемешанные фамилии детей.
# Гарантируется, что в группе нет однофамильцев.
# Формат вывода
# Количество учеников, которые любят только одну кашу.
# Если таких не окажется, в строке вывода нужно написать «Таких нет».
# Пример 1
# Ввод
# 3
# 2
# Васильев
# Петров
# Васечкин
# Иванов
# Михайлов
# Вывод
# 5
# Пример 2
# Ввод
# 3
# 3
# Иванов
# Петров
# Васечкин
# Иванов
# Петров
# Васечкин
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

lovers1porrige = set()
n, m = int(input()), int(input())
for _ in range(n + m):
    name = input()
    if name in lovers1porrige:
        lovers1porrige.remove(name)
    else:
        lovers1porrige.add(name)

if len(lovers1porrige):
    print(len(lovers1porrige))
else:
    print("Таких нет")
