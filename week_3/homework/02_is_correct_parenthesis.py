s = "(())()"


class Stack:
    __size = 0
    __top_idx = -1

    def __init__(self, size):
        self.__size = size
        self.__items = [None] * size
        return

    def push(self, value):
        self.__items[self.__top_idx + 1] = value
        self.__top_idx += 1
        return

    def peek(self) -> object:
        if self.__top_idx < 0:
            return None

        return self.__items[self.__top_idx]

    def pop(self) -> object:
        if self.__top_idx < 0:
            return None

        top_item = self.__items[self.__top_idx]
        self.__items[self.__top_idx] = None
        self.__top_idx -= 1

        return top_item

    def is_empty(self):
        return self.__top_idx < 0


def is_correct_parenthesis(string):
    stack = Stack(len(string))

    for i in range(len(string)):
        if string[i] == '(':
            stack.push(string[i])
        elif string[i] == ')':
            before = stack.pop()
            if before is None:
                return False
        else:
            print("Wrong character included:", string[i])
            return False

    return stack.is_empty()


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
