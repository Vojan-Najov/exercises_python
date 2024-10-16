# Зайка — 5
# 
# В долгой дороге дети вновь заскучали, и родителям приходится их развлекать
# поиском зверушек за окном. Давайте вместе с ними найдём заек.
# Формат ввода
# В первой строке указано натуральное число NN — количество выделенных
# придорожных местностей. В последующих строках записаны слова характеризующие
# выделенную местность.
# Информация о каждой местности завершается словом «ВСЁ».
# Формат вывода
# Количество местностей, в которых есть зайка.
#
# Пример 1
#
# Ввод
# 3
# березка
# елочка
# зайка
# волк
# березка
# ВСЁ
# сосна
# сосна
# сосна
# елочка
# грибочки
# медведь
# ВСЁ
# сосна
# сосна
# сосна
# белочка
# сосна
# белочка
# ВСЁ
# 
# Вывод
# 1
# 
# Пример 2
# Ввод
# 4
# зайка
# березка
# ВСЁ
# зайка
# зайка
# ВСЁ
# березка
# елочка
# березка
# ВСЁ
# елочка
# елочка
# елочка
# ВСЁ
# 
# Вывод
# 2
# 
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt

nn = int(input())
count = 0
for i in range(nn):
    local_count = 0
    while (s := input()) != "ВСЁ":
        if s == "зайка":
            local_count += 1
    if local_count:
        count += 1

print(count)

