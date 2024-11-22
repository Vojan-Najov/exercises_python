# Длина числа
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Разработайте функцию number_length, которая принимает одно целое число и
# возвращает его длину без учёта знака.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# result = number_length(12345)
# Вывод
# result = 5
# Пример 2
# Ввод
# result = number_length(-100500)
# Вывод
# result = 6

def number_length(num):
    if num in (-1, 0):
        return 1

    length = 0
    while num not in (-1, 0):
        length += 1
        num //= 10
    return length

if __name__ == '__main__':
    assert number_length(12345) == 5
    assert number_length(-100500) == 6
    assert number_length(0) == 1
    assert number_length(-1) == 1
    assert number_length(2) == 1
    assert number_length(-2) == 1

