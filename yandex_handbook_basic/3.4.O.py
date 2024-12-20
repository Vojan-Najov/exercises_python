# Список покупок 3.0
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt
# В этот раз семья договорилась о том, что в целях экономии бюджета, они будут
# совершать в день только три покупки. Напишите программу, которая готовит
# варианты списков покупок.
# Формат ввода
# В первой строке задано натуральное число N — количество членов семьи. В
# следующих N строках записаны желаемые продукты (через запятую и пробел).
# Формат вывода
# Варианты списков покупок в алфавитном порядке.
# Пример
# Ввод
# 2
# печенье, сушки
# чай, кофе
# Вывод
# кофе печенье сушки
# кофе печенье чай
# кофе сушки печенье
# кофе сушки чай
# кофе чай печенье
# кофе чай сушки
# печенье кофе сушки
# печенье кофе чай
# печенье сушки кофе
# печенье сушки чай
# печенье чай кофе
# печенье чай сушки
# сушки кофе печенье
# сушки кофе чай
# сушки печенье кофе
# сушки печенье чай
# сушки чай кофе
# сушки чай печенье
# чай кофе печенье
# чай кофе сушки
# чай печенье кофе
# чай печенье сушки
# чай сушки кофе
# чай сушки печенье

from itertools import permutations

for perm in permutations(sorted(x for _ in range(int(input())) for x in input().split(", ")), 3):
    print(*perm)
