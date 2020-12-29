input = "abcabcabcabcdededededede"


# sol.
# 1. 문제를 잘 읽어볼 것

def string_compression(string):
    length = len(string)
    compression_length_array = []

    for split_size in range(1, len(string) // 2 + 1):
        split = [string[i:i + split_size] for i in range(0, length, split_size)]
        split.append("")
        compressed = ""
        count = 1

        print(split_size, split)

        for j in range(1, len(split)):
            prev, cur = split[j - 1], split[j]
            if prev == cur:
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                count = 1

        print(split_size, "→", compressed)
        compression_length_array.append(len(compressed))

    return min(compression_length_array)


print(string_compression(input))  # 14 가 출력되어야 합니다!
