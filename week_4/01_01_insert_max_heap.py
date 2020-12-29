class MaxHeap:
    def __init__(self):
        self.items = [None]

    def get_parent_idx(self, child_idx):
        return child_idx // 2

    def insert(self, value):
        self.items.append(value)
        current_idx = len(self.items) - 1

        while current_idx > 1:
            parent_idx = current_idx // 2
            if self.items[parent_idx] < self.items[current_idx]:
                self.items[parent_idx], self.items[current_idx] = self.items[current_idx], self.items[parent_idx]
            current_idx = parent_idx

        print(self.items)

        return


# None 1 2 3 4 5 6

#      1
#   2     3
#  4 5   6 7
# 8 9

# 자식 찾기: i * 2 + 0~1
# 부모 찾기: i // 2

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
