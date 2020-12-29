numbers = [1, 1, 1, 1, 1]
target_number = 3


def is_to_target(array, target, cur_num, cur_idx):
    if cur_idx > len(array) - 1:
        if target == cur_num:
            return 1
        else:
            return 0

    plus = is_to_target(array, target, cur_num + array[cur_idx], cur_idx + 1)
    minus = is_to_target(array, target, cur_num - array[cur_idx], cur_idx + 1)
    return plus + minus


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    count = is_to_target(array, target, 0, 0)
    return count


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!