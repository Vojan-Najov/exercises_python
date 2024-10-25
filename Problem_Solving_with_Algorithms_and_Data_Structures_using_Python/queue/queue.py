class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    q = Queue()

    q.enqueue('dog')
    q.enqueue(4)
    q.enqueue(True)

    print(f"{q.isEmpty()=}")
    print(f"{q.size()=}")
    print(f"{q.dequeue()=}")
    print(f"{q.isEmpty()=}")
    print(f"{q.size()=}")
    print(f"{q.dequeue()=}")
    print(f"{q.isEmpty()=}")
    print(f"{q.size()=}")
    print(f"{q.dequeue()=}")
    print(f"{q.isEmpty()=}")
    print(f"{q.size()=}")
