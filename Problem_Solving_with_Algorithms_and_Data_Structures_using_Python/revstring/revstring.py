# run --> PYTHONPATH=$PYTHONPATH:stack python3 revstring/revstring.py
import stack


def revstring(string):
    s = stack.Stack()
    for latter in string:
        s.push(latter)
    
    rev = ""
    while not s.isEmpty():
        rev += s.pop()

    return rev

if __name__ == "__main__":
    s = "What a day"
    print(f"{s=} {revstring(s)=}")

    assert revstring("apple"), "elppa"
