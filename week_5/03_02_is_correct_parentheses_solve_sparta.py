from collections import deque

balanced_parentheses_string = "()))((()"


def is_correct_parenthesis(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0


def reverse_parenthesis(string):
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ')'
        else:
            reversed_string += '('
    return reversed_string


def separate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break
    v = ''.join(list(queue))
    return u, v


def change_to_correct_parenthesis(string):
    if string == "":
        return ""

    u, v = separate_to_u_v(string)
    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthesis(v)
    else:
        return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])


def get_correct_parentheses(string):
    if is_correct_parenthesis(string):
        return string
    else:
        return change_to_correct_parenthesis(string)


# "()(())()"가 반환 되어야 합니다!
print(get_correct_parentheses(balanced_parentheses_string))
