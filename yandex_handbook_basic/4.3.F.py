# Сортировка слиянием
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Мы уже реализовывали функцию merge, которая способна "слить" два
# отсортированных списка в один.
# Чаще всего её применяют в рекурсивном алгоритме сортировки слиянием.
# Напишите рекурсивную функцию merge_sort, которая производит сортировку списка.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций, за исключением рекурсивных.
# Трассировка вызова рекурсивной функции в обработке ответа не учитывается и
# показана для примера.
# Пример 1
# Ввод
# result = merge_sort([3, 2, 1])
# Вывод
# # Вызов merge_sort([3, 2, 1])
# # Вызов merge_sort([3])
# # Вызов merge_sort([2, 1])
# # Вызов merge_sort([2])
# # Вызов merge_sort([1])
# result = [1, 2, 3]
# Пример 2
# Ввод
# result = merge_sort([3, 1, 5, 3])
# Вывод
# # Вызов merge_sort([3, 1, 5, 3])
# # Вызов merge_sort([3, 1])
# # Вызов merge_sort([3])
# # Вызов merge_sort([1])
# # Вызов merge_sort([5, 3])
# # Вызов merge_sort([5])
# # Вызов merge_sort([3])
# result = [1, 3, 3, 5]

def merge_sort(alist):
    if len(alist) <= 1:
        return alist

    mid = len(alist) // 2
    lefthalf = alist[:mid]
    righthalf = alist[mid:]

    merge_sort(lefthalf)
    merge_sort(righthalf)

    i, j, k = 0, 0, 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            alist[k] = lefthalf[i]
            i += 1
        else:
            alist[k] = righthalf[j]
            j += 1
        k += 1

    while i < len(lefthalf):
        alist[k] = lefthalf[i]
        i += 1
        k += 1
    while j < len(righthalf):
        alist[k] = righthalf[j]
        j += 1
        k += 1

    return alist
    

if __name__ == '__main__':
    assert merge_sort([3, 2, 1]) == [1, 2, 3]
    assert merge_sort([3, 1, 5, 3]) == [1, 3, 3, 5]

