# Таблицы истинности 3
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt
# Продолжим работу с таблицами истинности.
# К сожалению, некоторые из операций Булевой алгебры не реализованы в Python.
# Самые частые не стандартные операции это: импликация, строгая дизъюнкция и
# эквивалентность.
# Обозначим их следующим образом:
#     импликация — ->;
#     строгая дизъюнкция — ^;
#     эквивалентность — ~.
# Напишите программу, которая для введённого сложного логического высказывания
# строит таблицу истинности.
# Формат ввода
# Вводится логическое выражение от нескольких переменных.
# Возможное содержание выражения:
#     Заглавная латинская буква — переменная;
#     not — отрицание;
#     and — конъюнкция;
#     or — дизъюнкция;
#     ^ — строгая дизъюнкция;
#     -> — импликация;
#     ~ — эквивалентность;
#     () — логические скобки.
# Формат вывода
# Выведите таблицу истинности данного выражения.
# Примечание
# Прежде, чем реализовывать новые операции, обратите внимание на их приоритет.
# Рекомендуем воспользоваться знаниями полученными при решении задачи
# «Польский калькулятор».
# Пример 1
# Ввод
# A -> B ~ C
# Вывод
# A B C F
# 0 0 0 0
# 0 0 1 1
# 0 1 0 0
# 0 1 1 1
# 1 0 0 1
# 1 0 1 0
# 1 1 0 0
# 1 1 1 1
# Пример 2
# Ввод
# A or C ~ not (A -> B) or C
# Вывод
# A B C F
# 0 0 0 1
# 0 0 1 1
# 0 1 0 1
# 0 1 1 1
# 1 0 0 1
# 1 0 1 1
# 1 1 0 0
# 1 1 1 1

from itertools import product

operations = {"not", "and", "or", "^", "->", "~"}
priority = {"not": 10, "and": 9, "or": 8, "^": 8, "->": 7, "~": 6, '(': 5}
names = {chr(ord('A') + i) for i in range(26)}

expr = input().replace('(', ' ( ').replace(')', ' ) ')
stack = []
queue = []
logvars = set()

for token in expr.split():
    if token in operations:
        while len(stack) and priority[stack[-1]] > priority[token]: 
            queue.insert(0, stack.pop())
        stack.append(token)
    elif token == '(':
        stack.append(token)
    elif token == ')':
        while len(stack) and stack[-1] != '(':
            queue.insert(0, stack.pop())
        if len(stack) == 0:
            exit("unpaired parethensis")
        stack.pop()
    elif token in names:
        queue.insert(0, token)
        logvars.add(token)
    else:
        exit(f"Error: {token}")

while len(stack):
    token = stack.pop()
    if token == '(':
        exit("unpaired parethensis")
    queue.insert(0, token)

print(" ".join(list(sorted(logvars)) + ['F']))

for comb in product((0, 1), repeat=len(logvars)):
    tmpqueue = queue[:]
    env = {x: y for x, y in zip(sorted(logvars), comb)}

    while len(tmpqueue):
        token = tmpqueue.pop()
        if token == 'not':
            operand = stack.pop()
            f = int(eval(f"not {operand}", env))
            stack.append(f)
        elif token == 'and':
            b, a = stack.pop(), stack.pop()
            f = int(eval(f"{a} and {b}", env))
            stack.append(f)
        elif token == 'or':
            b, a = stack.pop(), stack.pop()
            f = int(eval(f"{a} or {b}", env))
            stack.append(f)
        elif token == '^':
            b, a = stack.pop(), stack.pop()
            f = int(eval(f"not {a} and {b} or {a} and not {b}", env))
            stack.append(f)
        elif token == '->':
            b, a = stack.pop(), stack.pop()
            f = int(eval(f"not {a} or {b}", env))
            stack.append(f)
        elif token == '~':
            b, a = stack.pop(), stack.pop()
            f = int(eval(f"{a} == {b}", env))
            stack.append(f)
        else:
            stack.append(token)
            
    print(" ".join(map(str, list(comb) + [stack.pop()])))

