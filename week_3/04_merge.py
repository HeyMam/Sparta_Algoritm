array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    array_merge = [0] * (len(array_a) + len(array_b))
    i = 0
    j = 0
    while i < len(array_a) and j < len(array_b):
        if array_a[i] < array_b[j]:
            array_merge[i + j] = array_a[i]
            i += 1
        elif array_a[i] > array_b[j]:
            array_merge[i + j] = array_b[j]
            j += 1
        if not i < len(array_a):
            array_merge[i + j:len(array_merge)] = array_b[j:len(array_b)]
            j += len(array_b) - j
        if not j < len(array_b):
            array_merge[i + j:len(array_merge)] = array_a[i:len(array_a)]
            i += len(array_a) - i
        print(i, j, array_merge)
    return array_merge


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!