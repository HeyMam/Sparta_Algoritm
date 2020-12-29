class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    top = None

    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "Stack is empty."

        top = self.head
        self.head = top.next
        return top

    def peek(self):
        if self.is_empty():
            return "Stack is empty."

        return self.head

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None


s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek().data)
print(s.pop().data)
print(s.pop().data)
print(s.is_empty())
print(s.pop().data)
print(s.is_empty())
