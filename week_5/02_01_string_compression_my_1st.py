input = "abcabcabcabcdededededede"
import heapq


# abcabcabcabcdededededede  ->  24

# 4abc + dededededede       ->  16
# abc abc abc abc

# 2abcabc + 2dedede         ->  14


def string_compression_length(string, n):
    start = 0
    repeat_list = []
    after_string = ""

    while True:
        repeat = 1
        i = 0

        while True:
            if start + i + (n * repeat) >= len(string):
                break

            if string[start + i] != string[start + i + (n * repeat)]:
                break

            i += 1
            if i == n:
                repeat += 1
                i = 0

        if repeat > 1:
            repeat_list.append((repeat, string[start:start + n]))
            start += n * repeat
        else:
            break

    # 반복되는 문자열이 없었으면 원본 크기 그대로
    if len(repeat_list) <= 0:
        return len(string)

    # 압축 문자열 만들기
    last_repeated = 0
    for r, s in repeat_list:
        # print(after_string, str(r), s)
        after_string = after_string + str(r) + s
        last_repeated += r * n
    after_string = after_string + string[last_repeated:]

    return len(after_string)


def string_compression(string):
    min_len = []
    heapq.heappush(min_len, len(string))

    for n in range(1, len(string) // 2 + 1):
        heapq.heappush(min_len, string_compression_length(string, n))

    return heapq.heappop(min_len)
    # return 0


print(string_compression(input))  # 14 가 출력되어야 합니다!
