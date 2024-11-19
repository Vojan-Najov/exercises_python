# Файловая чистка
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Python в первую очередь скриптовый язык. Такие языки часто используются для
# создания консольных утилит.
# Напишите простую утилиту, которая очищает заданный файл от:
#     повторяющихся пробелов;
#     повторяющихся символов перевода строки;
#     табуляций,
#     излишних пробелов в начале и конце строк.
# Формат ввода
# Пользователь вводит два имени файлов.
# Входной файл содержит неформатированный текст произвольной длины.
# Формат вывода
# Во второй файл выведите очищенный текст.
# Пример
# Ввод
# # Пользовательский ввод:
# first.txt
# second.txt
# # Содержимое файла first.txt
#     очень 		 плохо форматированный       текст
# ну		ну	
# прямо
# очень-очень
# 	
# Вывод
# # Содержимое файла second.txt
# очень плохо форматированный текст
# нуну
# прямо
# очень-очень

infilename, outfilename = input(), input()
with open(infilename) as infile:
    with open(outfilename, "w") as outfile:
        for line in infile:
            last_smb = ""
            insert_space = False
            text_started = False
            for smb in line:
                if smb == '\t':
                    continue
                elif smb == '\n' and (last_smb == '\n' or not text_started):
                    continue
                elif smb == ' ':
                    insert_space = True
                    continue
                else:
                    if insert_space and text_started:
                        outfile.write(" ")
                    text_started = True
                    insert_space = False
                outfile.write(smb)
                last_smb = smb
