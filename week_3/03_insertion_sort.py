input_ex = [4, 6, 2, 9, 1]


def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            # print("i]", i, ", j]", j)
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
    return


insertion_sort(input_ex)
print(input_ex)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
