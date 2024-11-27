# Корень зла 2
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# В одной из первых лекций вы уже решали задачу о поиске корней уравнения.
# Давайте модернизируем её.
# Напишите функцию find_roots, принимающую три параметра: коэффициенты уравнения
# и возвращающую его корни в виде кортежа из двух значений.
# Так же создайте два собственных исключения NoSolutionsError и
# InfiniteSolutionsError, которые будут вызваны в случае отсутствия и
# бесконечного количества решений уравнения соответственно.
# Если переданные коэффициенты не являются рациональными числами, вызовите
# исключение TypeError.
# Примечание
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# print(find_roots(0, 0, 1))
# Вывод
# Вызвано исключение NoSolutionsError
# Пример 2
# Ввод
# print(find_roots(1, 2, 1))
# Вывод
# (-1.0, -1.0)

class InfiniteSolutionsError(Exception):
    pass


class NoSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if not (isinstance(a, (float, int)) and isinstance(b, (float, int)) and isinstance(c, (float, int))):
        raise TypeError('type error')

    if a == 0:
        if b == 0:
            if c == 0:
                raise InfiniteSolutionsError('infinity solutions')
            raise NoSolutionsError('no solutions')
        return (-c / b, -c / b)
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            raise NoSolutionsError('no solutions')
        d **= 0.5
        return ((-b - d) / (2 * a), (-b + d) / (2 * a))


if __name__ == '__main__':
    try:
        print(find_roots(0, 0, 1))
    except Exception as e:
        print(e)

    try:
        print(find_roots(1, 2, 1))
    except Exception as e:
        print(e)

    try:
        print(find_roots(0, 0, 0))
    except Exception as e:
        print(e)

    try:
        print(find_roots(1.0, '2', 1))
    except Exception as e:
        print(e)

