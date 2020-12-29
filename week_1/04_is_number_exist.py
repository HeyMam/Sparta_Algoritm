input = [3, 5, 6, 1, 2, 4]


# Big O 표기법으로는 소요시간 O(N)
# Big Omega 표기법으로는 소요시간 Ω(1)
def is_number_exist(number, array):

    for element in array:
        if element is number:
            return True

    return False


result = is_number_exist(3, input)
print(result)