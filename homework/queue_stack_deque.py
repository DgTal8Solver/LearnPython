class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Empty(Exception):
    def __init__(self):
        super().__init__("This is empty!")


class Stack:
    def __init__(self):
        self._head = None
        self._size = 0

    def put(self, value):
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def get(self):
        if self.is_empty():
            raise Empty
        value = self._head.value
        self._head = self._head.next
        self._size -= 1
        return value

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def put(self, value):
        new_node = Node(value)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def get(self):
        if self.is_empty():
            raise Empty
        value = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return value

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size


class Deque:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def put_left(self, value):
        new_node = DoubleNode(value)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._size += 1

    def put_right(self, value):
        new_node = DoubleNode(value)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def get_left(self):
        if self.is_empty():
            raise Empty
        value = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        else:
            self._head.prev = None
        self._size -= 1
        return value

    def get_right(self):
        if self.is_empty():
            raise Empty
        value = self._tail.value
        self._tail = self._tail.prev
        if self._tail is None:
            self._head = None
        else:
            self._tail.next = None
        self._size -= 1
        return value

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size


def main():
    # ----- Stack -----
    print("--- Stack ---")

    stack = Stack()
    print("Положили:", end=" ")
    for i in range(1, 6):
        print(i, end=" ")
        stack.put(i)
    
    print("\nРазмер:", stack.size())

    print("Получили:", end=" ")
    while not stack.is_empty():
        print(stack.get(), end=" ")
    print("\n")


    # ----- Queue -----
    print("--- Queue ---")

    queue = Queue()
    print("Положили:", end=" ")
    for ch in "abcde":
        print(ch, end=" ")
        queue.put(ch)
    
    print("\nРазмер:", queue.size())

    print("Получили:", end=" ")
    while not queue.is_empty():
        print(queue.get(), end=" ")
    print("\n")


    # ----- Deque -----
    print("--- Deque ---")

    dq = Deque()
    dq.put_right(10)
    dq.put_right(20)
    dq.put_left(5)
    dq.put_left(1)

    print("Deque слева направо:", end=" ")
    cur = dq._head
    while cur:
        print(cur.value, end=" ")
        cur = cur.next
    print("\nРазмер:", dq.size())
    print("Правый элемент:", dq.get_right())
    print("Левый элемент:", dq.get_left())
    print("Осталось элементов:", dq.size())


if __name__ == "__main__":
    main()