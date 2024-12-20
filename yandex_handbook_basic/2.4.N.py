# Числовая змейка
# Увы, обыкновенные прямоугольники детям быстро наскучили. Теперь
# воспитательнице требуется новая программа. Напишите программу, которая
# строит числовую змейку требуемого размера.
# Формат ввода
# В первой строке записано число NN — высота числового прямоугольника.
# Во второй строке указано число MM — ширина числового прямоугольника.
# Формат вывода
# Нужно вывести сформированную числовую змейку требуемого размера.
# Чтобы прямоугольник был красивым, каждый его столбец следует сделать
# одинаковой ширины.
# Пример 1
# Ввод
# 2
# 3
# Вывод
# 1 2 3
# 6 5 4
# Пример 2
# Ввод
# 4
# 6
# Вывод
#  1  2  3  4  5  6
# 12 11 10  9  8  7
# 13 14 15 16 17 18
# 24 23 22 21 20 19
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt

nn = int(input())
mm = int(input())
width = len(str(nn * mm))

for i in range(nn):
    if i % 2:
        for j in range(mm, 0, -1):
            print(f"{i * mm + j:{width}}", end=" ")
    else:
        for j in range(1, mm + 1):
            print(f"{i * mm + j:{width}}", end=" ")
    print()


