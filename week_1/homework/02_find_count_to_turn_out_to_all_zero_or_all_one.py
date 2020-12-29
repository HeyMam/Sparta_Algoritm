input_ex = "011110"
input_ex2 = "00111100110000100011111100"


# 0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다. 할 수 있는 행동은 문자
# 열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

# 예를 들어 s0001100 일 때,

# 전체를 뒤집으면 1110011이 된다.
# 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
# 하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로
# 만들 수 있다.

# 주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.


def find_count_to_turn_out_to_all_zero_or_all_one(string):

    block_count = [0, 0]    # 0 으로 이루어진 구간 개수, 1 로 이루어진 구간 개수
    current_block = '_'     # 현재 구간의 글자 (0 인지 1 인지)

    for char in string:
        if char != current_block:
            block_count[int(char)] += 1
            current_block = char

    min_block_count = 9223372036854775807

    for count in block_count:
        if count < min_block_count:
            min_block_count = count

    return min_block_count


result = find_count_to_turn_out_to_all_zero_or_all_one(input_ex)
print(result)