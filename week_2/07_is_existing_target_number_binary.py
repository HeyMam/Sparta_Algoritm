finding_target = 3
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


def find_number_in_range(target, numbers, first, last):

    if last < first:
        return False

    middle = (first + last) // 2

    if numbers[middle] == target:
        return True

    return find_number_in_range(target, numbers, first, middle - 1) or find_number_in_range(target, numbers, middle + 1, last)


def is_exist_target_number_binary(target, numbers):
    return find_number_in_range(target, numbers, 0, len(numbers) - 1)


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)