input_ex = "abadabac"


def find_not_repeating_character(string):

    alphabet = [0] * 26

    for char in string:
        alphabet[ord(char) - ord('a')] += 1

    for char in string:
        if alphabet[ord(char) - ord('a')] == 1:
            return char

    return '_'


result = find_not_repeating_character(input_ex)
print(result)