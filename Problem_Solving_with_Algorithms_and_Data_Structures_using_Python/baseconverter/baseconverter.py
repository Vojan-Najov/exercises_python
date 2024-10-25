# run --> PYTHONPATH=$PYTHONPATH:stack python3 baseconverter/baseconverter.py

from stack import Stack

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber //= 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

def baseConverter(decNumber, base):
    assert 2 <= base <= 16
    digits = "0123456789ABCDEF"

    remstack = Stack()
    sign = False
    if decNumber < 0:
        decNumber = -decNumber
        sign = True

    while decNumber:
        rem = decNumber % base
        remstack.push(rem)
        decNumber //= base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString if not sign else "-" + newString

if __name__ == "__main__":
    print(divideBy2(42))
    print(baseConverter(-25, 2))
    print(baseConverter(25, 2))
    print(baseConverter(25, 8))
    print(baseConverter(25, 16))


