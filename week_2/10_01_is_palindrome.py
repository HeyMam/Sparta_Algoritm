input = "abcba"


def is_palindrome(string):
    length = len(string)
    middle = length // 2
    repeat = 0

    for i in range(middle):
        if string[i] != string[length - 1 - i]:
            return False

    return True


print(is_palindrome(input))