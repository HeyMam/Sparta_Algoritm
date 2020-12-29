class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        last = len(self.items) - 1
        if last < 1:
            return None

        self.items[1], self.items[last] = self.items[last], self.items[1]
        result = self.items.pop(last)

        current_idx = 1
        last = last - 1

        while current_idx * 2 < last:
            left_idx = current_idx * 2
            right_idx = current_idx * 2 + 1
            max_idx = current_idx

            if self.items[left_idx] > self.items[max_idx]:
                max_idx = left_idx

            if right_idx <= last and self.items[right_idx] > self.items[max_idx]:
                max_idx = right_idx

            if max_idx == current_idx:
                break

            self.items[max_idx], self.items[current_idx] = self.items[current_idx], self.items[max_idx]
            current_idx = max_idx

        return result  # 8 을 반환해야 합니다.


#      8
#    7   6
#   2 5 4

#      8
#    7   6
#   2 5 4

max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]
