# Разделяй и властвуй
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Напишите утилиту, которая разделяет числа, записанные в файле, на три группы:
#     числа с преобладающим количеством чётных цифр;
#     числа с преобладающим количеством нечётных цифр;
#     числа с одинаковым количеством чётных и нечётных цифр.
# Формат ввода
# Пользователь вводит четыре имени файла.
# Первый файл содержит произвольное количество чисел, разделённых пробелами и
# символами перевода строки.
# Формат вывода
# В три другие файла выведите числа, которые подходят под требуемое условие.
# Сохраните положение чисел в строках.
# Пример
# Ввод
# # Пользовательский ввод:
# numbers.txt
# even.txt
# odd.txt
# eq.txt
# # Содержимое файла numbers.txt
# 650975472 591084323 629700 1504180 577023
# 8460612246 42161437 29409368 58531725 5725268 2198001838
# 796451 69358 7195510 975628465 9756641
# 44200289 126541 979391 93479581 291170 28987042 86139603
# Вывод
# # Содержимое файла even.txt
# 629700 1504180
# 8460612246 29409368 5725268 2198001838
# 975628465
# 44200289 28987042
# # Содержимое файла odd.txt
# 650975472 591084323 577023
# 58531725
# 796451 69358 7195510 9756641
# 979391 93479581 291170
# # Содержимое файла eq.txt
# 42161437
# 126541 86139603

finname, foutname1, foutname2, foutname3 = input(), input(), input(), input()
with open(finname) as fin:
    with open(foutname1, "w") as out1:
        with open(foutname2, "w") as out2:
            with open(foutname3, "w") as out3:
                for line in fin:
                    first1, first2, first3 = True, True, True
                    for word in line.split():
                        num = int(word)
                        even = 0
                        odd = 0
                        while num:
                            digit = num % 10
                            if digit % 2:
                                odd += 1
                            else:
                                even += 1
                            num //= 10
                        if even > odd:
                            if not first1:
                                out1.write(" ")
                            out1.write(word)
                            first1 = False
                        elif even < odd:
                            if not first2:
                                out2.write(" ")
                            out2.write(word)
                            first2 = False
                        else:
                            if not first3:
                                out3.write(" ")
                            out3.write(word)
                            first3 = False
                    out1.write('\n')
                    out2.write('\n')
                    out3.write('\n')



