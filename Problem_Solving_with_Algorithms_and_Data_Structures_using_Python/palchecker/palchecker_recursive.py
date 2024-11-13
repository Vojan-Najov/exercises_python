
def palchecker(aString):
    aString = aString.lower()
    for smb in " .,!:;-?'\"":
        aString = aString.replace(smb, "")

    if len(aString) < 2:
        return True
    else:
        return aString[0] == aString[-1] and palchecker(aString[1:-1])

if __name__ == "__main__":
    print(palchecker("kayak"))
    print(palchecker("aibohphobia"))
    print(palchecker("Live not on evil"))
    print(palchecker("Reviled did I live, said I, as evil I did deliver"))
    print(palchecker("Go hang a salami; I'm a lasagna hog."))
    print(palchecker("Able was I ere I saw Elba"))
    print(palchecker("Kanakanak"))
    print(palchecker("Wassamassaw"))


