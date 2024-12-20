# run --> PYTHONPATH=$PYTHONPATH:stack python3 infixtopostfix/infixtopostfix.py

from stack import Stack

def infixToPostfix(infixexpr):
    prec = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "^":
        return op1 ** op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

if __name__ == "__main__":
    print(infixToPostfix("A * B + C * D"))
    print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(infixToPostfix("( A + B ) * ( C + D )"))
    print(infixToPostfix("( A + B ) * C"))
    print(infixToPostfix("A + B * C"))
    print(infixToPostfix("9 + 3 * 5 / ( 8 - 4 )"))
    print(infixToPostfix("5 * 3 ^ ( 4 - 2 )"))
    print(infixToPostfix("2 ^ 3 ^ 4"))


    print(postfixEval("7 8 + 3 2 + /"))
