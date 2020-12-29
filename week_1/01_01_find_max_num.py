numbers = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max_num: int = array[0]
    for i in range(len(array)):
        if array[i] > max_num:
            max_num = array[i]
    return max_num


result = find_max_num(numbers)
print(result)