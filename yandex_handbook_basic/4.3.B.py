# Рекурсивный сумматор цифр
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Рекурсия – отличный способ избавиться от циклов, особенно от while. Давайте
# вспомним одну из наших старых задач и модернизируем её.
# Напишите функцию recursive_digit_sum, которая находит сумму всех цифр
# натурального числа.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций, за исключением рекурсивных.
# Трассировка вызова рекурсивной функции в обработке ответа не учитывается и
# показана для примера.
# Пример 1
# Ввод
# result = recursive_digit_sum(123)
# Вывод
# # Вызов recursive_digit_sum(123)
# # Вызов recursive_digit_sum(12)
# # Вызов recursive_digit_sum(1)
# # Вызов recursive_digit_sum(0)
# result = 6
# Пример 2
# Ввод
# result = recursive_digit_sum(7321346)
# Вывод
# # Вызов recursive_digit_sum(7321346)
# # Вызов recursive_digit_sum(732134)
# # Вызов recursive_digit_sum(73213)
# # Вызов recursive_digit_sum(7321)
# # Вызов recursive_digit_sum(732)
# # Вызов recursive_digit_sum(73)
# # Вызов recursive_digit_sum(7)
# # Вызов recursive_digit_sum(0)
# result = 26

def recursive_digit_sum(num):
    num = abs(num)
    if num < 10:
        return abs(num)
    return num % 10 + recursive_digit_sum(num // 10)


if __name__ == '__main__':
    assert recursive_digit_sum(123) == 6
    assert recursive_digit_sum(7321346) == 26
