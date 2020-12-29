input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):

    max_value = -1

    for i in range(len(array)):
        if i == 0:
            max_value = array[0]
            continue

        if array[i] <= 1 or max_value == 0:
            max_value += array[i]
        else:
            max_value *= array[i]

    return max_value


result = find_max_plus_or_multiply(input)
print(result)