# run -> PYTHONPATH=$PATHONPATH python3 parchecker/parchecker.py

from stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        elif symbol in ")]}":
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1

    return balanced and s.isEmpty()

def matches(open, close):
    opens = ('(', '[', '{', )
    closers = (')', ']', '}', )
    return opens.index(open) == closers.index(close)

if __name__ == "__main__":
    print(parChecker('(((1 + 2))())'))
    print(parChecker('(()'))
    
    print(parChecker('{{([][1, 2])}()}'))
    print(parChecker('[{()]'))
