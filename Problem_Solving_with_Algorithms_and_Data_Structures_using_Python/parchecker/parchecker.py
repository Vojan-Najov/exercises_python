# run -> PYTHONPATH=$PATHONPATH python3 parchecker/parchecker.py

from stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        elif symbol == ")":
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1

    return balanced and s.isEmpty()

if __name__ == "__main__":
    print(parChecker('(((1 + 2))())'))
    print(parChecker('(()'))
