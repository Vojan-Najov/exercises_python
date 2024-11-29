# Шаг навстречу
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Два выдуманных человечка Дека и Поля, пользуются каждый своей системой
# координат. Деке нравится представлять себя в декартовом пространстве, а
# Поле — в полярном.
# Напишите программу, определяющую кратчайшее расстояние, которое нужно пройти
# Деке и Поле, чтобы встретиться.
# Формат ввода
# В первой строке записаны координаты Деки: два рациональных числа — x и y
# Во второй строке записаны координаты Поли: два рациональных числа — ρ и ϕ
# Формат вывода
# Одно число — расстояние между Декой и Полей.
# Примечание
# Дека и Поля живут на одной плоскости с общим центром.
# ϕ — измеряется в радианах.
# Пример 1
# Ввод
# -7 20
# 7 3.141592653589793
# Вывод
# 20.0
# Пример 2
# Ввод
# 10 10
# 10.142135623730951 0.7853981633974483
# Вывод
# 3.9999999999999996

from math import dist, cos, sin

x, y = (float(x) for x in input().split())
p, f = (float(x) for x in input().split())
p, f = p * cos(f), p * sin(f)
print(dist((x, y), (p, f)))