class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0
        while cur_index < index:
            if cur is None:
                break
            cur_index += 1
            cur = cur.next
        return cur

    def add_node(self, index, data):
        bef = None
        cur = self.head
        cur_index = 0

        while cur_index < index:
            if cur is None:
                break
            cur_index += 1
            bef = cur
            cur = cur.next

        new_node = Node(data)
        new_node.next = cur

        if bef is None:
            self.head = new_node
        else:
            bef.next = new_node

        return


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.add_node(2, 2.5)
linked_list.add_node(0, 0.5)

linked_list.print_all()
