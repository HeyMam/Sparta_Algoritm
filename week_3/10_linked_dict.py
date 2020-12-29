class LinkedTuple:
    def __init__(self):
        self.items = []  # list() 와 동일

    def add(self, key, value):
        self.items.append((key, value))
        return

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % 8
        self.items[index].add(key, value)
        return

    def get(self, key):
        index = hash(key) % 8
        return self.items[index].get(key)


my_dict = LinkedDict()
my_dict.put("test", 3)
my_dict.put("test1", 4)
print(my_dict.get("test1"))
