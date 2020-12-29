input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    max_occurred_index = 0

    for char in string:
        if char.isalpha():
            index = ord(char) - ord('a')
            alphabet_occurrence_array[index] += 1

    for i in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[i] > alphabet_occurrence_array[max_occurred_index]:
            max_occurred_index = i

    return chr(max_occurred_index + ord('a'))


result = find_max_occurred_alphabet(input)
print(result)