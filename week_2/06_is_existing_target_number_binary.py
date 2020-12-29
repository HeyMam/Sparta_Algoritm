finding_target = 1
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    first = 0
    last = len(array) - 1

    while first <= last:
        middle = (first + last) // 2
        print("middle: [", middle, "] ", array[middle], sep='')

        if array[middle] > target:      # target 이 왼쪽에 있음
            last = middle - 1
        elif array[middle] < target:    # target 이 오른쪽에 있음
            first = middle + 1
        else:
            return True

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)