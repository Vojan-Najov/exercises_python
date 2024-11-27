# Слияние с проверкой
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Когда-то вы уже писали функцию merge, которая производит слияние двух
# отсортированных кортежей.
# Давай-те её немного переработаем.
# Введём систему проверок:
#     если один из параметров не является итерируемым объектом, то вызовите
#     исключение StopIteration;
#     если значения входных параметров содержат «неоднородные» данные, то
#     вызовите исключение TypeError;
#     если один из параметров не отсортирован, то вызовите исключение ValueError.
# Проверки следует проводить в указанном порядке.
# Если параметры прошли все проверки, верните итерируемый объект, являющийся
# слиянием двух переданных.
# Примечание
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# print(*merge(35, (1, 2, 3)))
# Вывод
# Вызвано исключение StopIteration
# Пример 2
# Ввод
# print(*merge([3, 2, 1], range(10)))
# Вывод
# Вызвано исключение ValueError

def check_iterable(x):
    try:
        iter(x)
    except Exception:
        raise StopIteration('stop iteration')


def merge(a, b):
    check_iterable(a)
    check_iterable(b)

    res = []
    i, j = 0, 0
    prev_type = None
    prev_a = None
    prev_b = None

    while i < len(a) and j < len(b):
        if prev_type is not None and (not isinstance(a[i], prev_type) or not isinstance(b[j], prev_type)):
            raise TypeError('type error')
        if prev_a is not None and a[i] < prev_a:
            raise ValueError('value error')
        if prev_b is not None and b[j] < prev_b:
            raise ValueError('value error')

        if a[i] < b[j]:
            res.append(a[i])
            prev_type = type(a[i])
            prev_a = a[i]
            i += 1
        else:
            res.append(b[j])
            prev_type = type(b[j])
            prev_b = b[j]
            j += 1

    while i < len(a):
        if prev_type is not None and not isinstance(a[i], prev_type):
            raise TypeError('type error')
        if prev_a is not None and a[i] < prev_a:
            raise ValueError('value error')
        res.append(a[i])
        prev_type = type(a[i])
        prev_a = a[i]
        i += 1
    while j < len(b):
        if prev_type is not None and not isinstance(b[j], prev_type):
            raise TypeError('type error')
        if prev_b is not None and b[j] < prev_b:
            raise ValueError('value error')
        res.append(b[j])
        prev_type = type(b[j])
        prev_b = b[j]
        j += 1

    return tuple(res)


if __name__ == '__main__':

    assert merge((1, 2), (3, 4, 5)) == (1, 2, 3, 4, 5)
    assert merge((7, 12), (1, 9, 50)) == (1, 7, 9, 12, 50)
    
    try:
        print(*merge(35, (1, 2, 3)))
    except Exception as e:
        print(e)

    try:
        print(*merge([3, 2, 1], range(10)))
    except Exception as e:
        print(e)

    try:
        print(*merge([1, 'a'], range(10)))
    except Exception as e:
        print(e)

