def print_alphabet_array():
    print('[', end='')
    for i in range(0, 26):
        if i != 25:
            print(chr(ord('a') + i), end=', ', flush=True)
        else:
            print(chr(ord('a') + i), ']', sep='')


def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if char.isalpha():
            num = ord(char) - ord('a')
            alphabet_occurrence_array[num] += 1

    return alphabet_occurrence_array


print_alphabet_array()
print(find_alphabet_occurrence_array("hello my name is sparta"))
