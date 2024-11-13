
def toStr(num, base):
    convertString = "0123456789ABCDEF"
    if num < base:
        return convertString[num]
    else:
        return toStr(num // base, base) + convertString[num % base]

if __name__ == "__main__":
    print(toStr(187, 2))
