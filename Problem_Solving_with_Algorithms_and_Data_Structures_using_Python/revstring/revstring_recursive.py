
def revstring_recursive(string):
    if len(string) < 2:
        return string
    else:
        return revstring_recursive(string[1:]) + string[0]

if __name__ == "__main__":

    print(revstring_recursive("hello") == "olleh")
    print(revstring_recursive("l") == "l")
    print(revstring_recursive("follow") == "wollof")
    print(revstring_recursive("") == "")
