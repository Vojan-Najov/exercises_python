#!/usr/bin/env python3

#Таблица умножения
#
#Местная фабрика канцелярских товаров заказала у вас программу, которая
#генерирует таблицы умножения.
#Давайте поддержим локального производителя!
#Формат ввода
#
#Вводится одно натуральное число — требуемый размер таблицы.
#Формат вывода
#
#Таблица умножения заданного размера.

n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=" ")
    print()


