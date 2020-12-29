from collections import deque

balanced_parentheses_string = "()))((()"


# 1. "(()())()"   ->  "(()())()"

# 2. ")("         ->  "()"

# 3. "()))((()"   ->  "()(())()"
#    () ))((()
#    ()  +   ))((    +   ()
#    ()  +   ( () )    +   ()
#    ()  +   (())()
#    ()(())()

def is_correct_string(string):
    balance = 0
    for i in range(len(string)):
        char = string[i]
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        # ')' 괄호가 더 먼저 나오면
        if balance < 0:
            return False
    return balance == 0


def get_reverse_parentheses(string):
    result = ""

    for i in range(len(string)):
        char = string[i]
        if char == '(':
            result = result + ')'
        elif char == ')':
            result = result + '('

    return result


def get_correct_parentheses(string):
    if string == "":
        return ""

    u = ""
    v = ""
    balance = 0

    # 균형잡힌 최소 단위 u 찾기
    for i in range(len(string)):
        char = string[i]

        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1

        # 규형잡혀 있다면
        if balance == 0:
            u = string[0:i + 1]
            v = string[i + 1:]
            break

    print("Split:", u, v, is_correct_string(u))

    if is_correct_string(u):
        return u + get_correct_parentheses(v)
    else:
        return "(" + get_correct_parentheses(v) + ")" + get_reverse_parentheses(u[1:-1])


# "()(())()"가 반환 되어야 합니다!
print(get_correct_parentheses(balanced_parentheses_string))
