class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node
        return

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        return_node = self.head
        self.head = return_node.next

        return return_node

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        return self.head

    def is_empty(self):
        return self.head is None

    def print(self):
        if self.is_empty():
            return

        current = self.head
        print("[", sep='', end='')
        while current is not None:
            print(current.data, sep='', end=' ')
            current = current.next
        print("\b]")
        return


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.print()
print("Dequeue:", q.dequeue().data)
print("Dequeue:", q.dequeue().data)
print("Peek:", q.peek().data)
print("Dequeue:", q.dequeue().data)
q.enqueue(60)
q.enqueue(70)
print("Dequeue:", q.dequeue().data)
print("Dequeue:", q.dequeue().data)
print("Peek:", q.peek().data)
print("Dequeue:", q.dequeue().data)
print("Dequeue:", q.dequeue().data)
q.dequeue()
q.peek()
