# Множество нечетных чисел
# Вашему решению будет предоставлен список numbers, содержащий натуральные
# числа.
# Напишите выражение для генерации множества всех нечётных чисел среди
# переданных.
# Примечание
# В решении не должно быть ничего, кроме выражения.
# Пример 1
# Ввод
# numbers = [1, 2, 3, 4, 5]
# Вывод
# {1, 3, 5}
# Пример 2
# Ввод
# numbers = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]
# Вывод
# {1, 3}
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод

numbers = [int(num) for num in input().split(" = ")[1].strip("[]").split(", ")]
odd = {num for num in numbers if num % 2}
print(odd)
