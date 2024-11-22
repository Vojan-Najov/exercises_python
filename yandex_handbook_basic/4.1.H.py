# А роза упала на лапу Азора 7.0
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Напишите функцию is_palindrome, которая принимает натуральное число, строку,
# кортеж или список, а возвращает логическое значение: True — если передан
# палиндром, а в противном случае — False.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Для определения типа параметра можно воспользоваться функцией type или более
# продвинутой isinstance.
# Пример 1
# Ввод
# result = is_palindrome(123)
# Вывод
# result = False
# Пример 2
# Ввод
# result = is_palindrome([1, 2, 1, 2, 1])
# Вывод
# result = True

def is_palindrome(arg):
    if isinstance(arg, int):
        revnum = 0
        num = abs(arg)
        arg = abs(arg)
        while arg:
            revnum *= 10
            revnum += arg % 10
            arg //= 10
        return num == revnum
    else:
        left, right = 0, len(arg) - 1
        eq = True
        while left < right and eq:
            if arg[left] != arg[right]:
                eq = False
            left += 1
            right -= 1
        return eq

if __name__ == '__main__':
    assert is_palindrome(123) == False
    assert is_palindrome(12321) == True
    assert is_palindrome(-12344321) == True
    assert is_palindrome([1, 2, 1, 2, 1]) == True
    assert is_palindrome([1, 2, 1, 3, 2, 1]) == False
    assert is_palindrome("abcba") == True
    assert is_palindrome("acba") == False


