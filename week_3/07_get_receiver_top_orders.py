top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    orders = [0] * len(heights)
    # for i in range(len(heights) - 1, -1, -1):
    #     for j in range(i - 1, -1, -1):
    #         if heights[j] > heights[i]:
    #             orders[i] = j + 1
    #             break
    while heights:
        height = heights.pop()
        for j in range(len(heights) - 1, -1, -1):
            if heights[j] > height:
                orders[len(heights)] = j + 1
                break

    return orders


# [0, 0, 2, 2, 4] 가 반환되어야 한다!
print(get_receiver_top_orders(top_heights))

# 인덱스 기준
# [-1, -1, 1, 1, 3]
