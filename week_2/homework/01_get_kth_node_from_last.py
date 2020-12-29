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

    def count(self):
        cur = self.head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def find(self, idx):
        if idx < 0:
            print("Index must be positive:", idx)
        if idx >= self.count() - 1:
            print("Overflowed Index:", idx)

        cur_idx = 0
        cur = self.head
        while cur is None or cur_idx < idx:
            cur = cur.next
            cur_idx += 1
        return cur

    def get_kth_node_from_last(self, k):
        count = self.count()
        return self.find(count - k)


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
