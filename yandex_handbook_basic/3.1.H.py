# Зайка — 7
# Вновь поищем заек за окном поезда.
# Формат ввода
# В первой строке записано натуральное число NN — количество выделенных
# придорожных местностей.
# В каждой из NN последующих строк записано описание придорожной местности.
# Формат вывода
# Для каждой строки нужно найти положение первого зайки.
# Если в строке нет заек, то об этом нужно непременно сообщить.
# Примечание
# Для символов в строках используйте нумерацию с 1.
# Пример 1
# Ввод
# 3
# березка елочка зайка волк березка
# сосна зайка сосна елочка зайка медведь
# сосна сосна сосна белочка сосна белочка
# Вывод
# 16
# 7
# Заек нет =(
# Пример 2
# Ввод
# 4
# зайка березка
# березка зайка
# березка елочка березка
# елочка елочка елочка
# Вывод
# 1
# 9
# Заек нет =(
# Заек нет =(
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt

n = int(input())
for _ in range(n):
    s = input()
    idx = s.lower().find("зайка")
    if idx == -1:
        print("Заек нет =(")
    else:
        print(idx + 1)

