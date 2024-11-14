# Это будет шедевр!
# Главный повар детского сада хочет быстрее выбирать блюда для готовки.
# В его распоряжении есть список продуктов, а также набор блюд.
# Напишите программу, способную быстро определить блюда, которые можно
# приготовить.
# Формат ввода
# Число продуктов (N), которые имеются в наличии.
# N строк с названиями продуктов.
# Число рецептов (M), о которых имеется информация.
# M блоков строк для каждого из рецептов.
# В первой строке каждого блока записано название блюда.
# Во второй — число ингредиентов.
# Затем перечисляются сами ингредиенты, требуемые для приготовления блюда.
# Формат вывода
# Список блюд, которые можно приготовить в алфавитном порядке.
# Если ни одно из блюд нельзя приготовить, следует вывести «Готовить нечего».
# Пример 1
# Ввод
# 4
# Яблоки
# Хлеб
# Варенье
# Картошка
# 3
# Тосты
# 2
# Хлеб
# Варенье
# Яблочный Сок
# 1
# Яблоки
# Яичница
# 1
# Яйца
# Вывод
# Тосты
# Яблочный Сок
# Пример 2
# Ввод
# 1
# хлеб
# 1
# бутерброд
# 2
# масло
# хлеб
# Вывод
# Готовить нечего
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt

n = int(input())
ingredients = set()
for _ in range(n):
    ingredients.add(input())

m = int(input())
dishes = {}
for _ in range(m):
    title = input()
    n = int(input())
    s = set()
    for _ in range(n):
        s.add(input())
    dishes[title] = s

lst = [title for title in dishes if dishes[title] <= ingredients]
print("\n".join(sorted(lst)) if len(lst) else "Готовить нечего")


