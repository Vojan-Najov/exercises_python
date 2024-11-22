# Числовая строка
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Разработайте функцию split_numbers, которая принимает строку целых чисел,
# разделённых пробелами, и возвращает кортеж из этих чисел.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Вы можете спросить: почему кортеж, а не список. Всё дело в безопасности.
# Кортежи неизменяемые коллекции и их безопаснее передавать в функцию или из неё.
# Пример 1
# Ввод
# result = split_numbers("1 2 3 4 5")
# Вывод
# result = (1, 2, 3, 4, 5)
# Пример 2
# Ввод
# result = split_numbers("1 -2 3 -4 5")
# Вывод
# result = (1, -2, 3, -4, 5)

def split_numbers(string):
    return tuple(int(word) for word in string.split())

if __name__ == '__main__':
    assert split_numbers("1 2 3 4 5") == (1, 2, 3, 4, 5)
    assert split_numbers("1 -2 3 -4 5") == (1, -2, 3, -4, 5)