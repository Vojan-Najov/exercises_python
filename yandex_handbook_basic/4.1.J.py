# Слияние
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Напишите функцию merge, которая принимает два отсортированных по возрастанию
# кортежа целых чисел, а возвращает один из всех переданных чисел.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# В этой задаче отключены стандартные сортировки
# Пример 1
# Ввод
# result = merge((1, 2), (3, 4, 5))
# Вывод
# result = (1, 2, 3, 4, 5)
# Пример 2
# Ввод
# result = merge((7, 12), (1, 9, 50))
# Вывод
# result = (1, 7, 9, 12, 50)

def merge(atuple1, atuple2):
    alist = []
    i, j = 0, 0
    while i < len(atuple1) and j < len(atuple2):
        if atuple1[i] < atuple2[j]:
            alist.append(atuple1[i])
            i += 1
        else:
            alist.append(atuple2[j])
            j += 1
    while i < len(atuple1):
        alist.append(atuple1[i])
        i += 1
    while j < len(atuple2):
        alist.append(atuple2[j])
        j += 1
    return tuple(alist)

if __name__ == '__main__':

    assert merge((1, 2), (3, 4, 5)) == (1, 2, 3, 4, 5)
    assert merge((7, 12), (1, 9, 50)) == (1, 7, 9, 12, 50)
