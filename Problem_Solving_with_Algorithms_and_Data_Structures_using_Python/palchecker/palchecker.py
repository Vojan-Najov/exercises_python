# run --> PYTHONPATH=$PYTHONPATH:deque python3 palchecker/palchecker.py

from deque import Deque

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        stillEqual = first == last

    return stillEqual

if __name__ == "__main__":
    print(palchecker("lsdkjfaser"))
    print(palchecker("radar"))
