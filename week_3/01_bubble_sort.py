input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    for x in range(len(array) - 1):
        for i in range(len(array) - 1 - x):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

# 5 4 3 2 1         0   range: [0 : 3] == [0 : last_idx - 1]
#           0 ~ 3       range: [0 : 3 - x] == [0 : last_idx - 1 - x]
# 4 3 2 1 5         1
#           0 ~ 2
# 3 2 1 4 5         2
#           0 ~ 1
# 2 1 3 4 5         3
#           0
# 2 1 3 4 5
