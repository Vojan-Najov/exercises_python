# Простая задача 5.0
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Напишите функцию is_prime, которая принимает натуральное число, а возвращает
# булево значение: True — если переданное число простое, а иначе — False.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# result = is_prime(1001459)
# Вывод
# result = True
# Пример 2
# Ввод
# result = is_prime(79701)
# Вывод
# result = False

def is_prime(num):
    for n in range(2, int(num ** 0.5)):
        if num % n == 0:
            return False
    return True

if __name__ == '__main__':
    assert is_prime(1001459) == True
    assert is_prime(79701) == False
