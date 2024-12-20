# Чётная фильтрация
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Напишите lambda выражение для фильтрации чисел с чётной суммой цифр.
# Примечание
# В решении не должно быть ничего, кроме выражения.
# Пример 1
# Ввод
# print(*filter(<ваше выражение>, (1, 2, 3, 4, 5)))
# Вывод
# 2 4
# Пример 2
# Ввод
# print(*filter(<ваше выражение>, (32, 64, 128, 256, 512)))
# Вывод
# 64 512

myfilter = lambda x: sum(int(d) for d in str(x) if d.isnumeric()) % 2 == 0

print(*filter(myfilter, (1, 2, 3, 4, 5)))
print(*filter(myfilter, (32, 64, 128, 256, -512)))
