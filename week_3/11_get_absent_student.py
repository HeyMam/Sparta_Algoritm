all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

class HashTable:
    __length = 0
    __items = []

    def __init__(self, len):
        self.__length = len
        self.__items = [None] * len
        return

    def push(self, key, value):
        index = hash(key) % self.__length
        self.__items[index] = value

    def get(self, key):
        index = hash(key) % self.__length
        return self.__items[index]


def get_absent_student(all_array, present_array):

    # s = HashTable(len(present_array)) # 강의실에 있는 학생들
    # for i in range(len(present_array)):
    #     s.push(present_array[i], present_array[i])
    # for i in range(len(all_array)):
    #     if s.get(all_array[i]) is None:
    #         return all_array[i]

    d = dict()  # 강의실에 있는 학생들
    for i in range(len(present_array)):
        d[present_array[i]] = present_array[i]

    for i in range(len(all_array)):
        if d.get(all_array[i]) is None:
            return all_array[i]

    return None


print(get_absent_student(all_students, present_students))