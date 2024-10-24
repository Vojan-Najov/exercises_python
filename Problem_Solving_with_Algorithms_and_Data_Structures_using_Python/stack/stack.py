
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    s = Stack()
    print(f"{s.isEmpty()=}")
    s.push(4)
    s.push("dog")
    print(f"{s.peek()}")
    s.push(True)
    print(f"{s.size()=}")
    print(f"{s.isEmpty()=}")
    print(f"{s.pop()}")
    print(f"{s.pop()}")
    print(f"{s.size()}")

