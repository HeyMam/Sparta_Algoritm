import itertools, sys, time

# # Test Case 1
# # Answer: 5
# n = 5
# m = 3
#
# city_map = [
#     [0, 0, 1, 0, 0],
#     [0, 0, 2, 0, 1],
#     [0, 1, 2, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 2],
# ]

# # # Test Case 2
# # Answer: 10
# n = 5
# m = 2
#
# city_map = [
#     [0, 2, 0, 1, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [2, 0, 0, 1, 1],
#     [2, 2, 0, 1, 2],
# ]


# Test Case 4
# Answer: 32
n = 5
m = 1

city_map = [
    [1, 2, 0, 2, 1],
    [1, 2, 0, 2, 1],
    [1, 2, 0, 2, 1],
    [1, 2, 0, 2, 1],
    [1, 2, 0, 2, 1],
]


# 0: 빈칸
# 1: 집
# 2: 치킨집

# 2 <= N <= 50  - 도시 가로/세로 크기
# 1 <= M <= 13  - 페업 시키지 않을 치킨집 최대 수
# 1 <= 집의 개수 <= 2N
# 치킨 집 최대 M개를 골랐을 때, 치킨 거리의 최솟값 출력하기


def get_distance(tuple1, tuple2):
    return abs(tuple1[0] - tuple2[0]) + abs(tuple1[1] - tuple2[1])


def find_closest_distance(source_idx, source_pos_list, target_idx_list, target_pos_list, record):
    distance = 0
    min_distance = sys.maxsize
    for target_idx in target_idx_list:
        distance = record[source_idx][target_idx]
        if distance == -1:
            distance = get_distance(source_pos_list[source_idx], target_pos_list[target_idx])
            record[source_idx][target_idx] = distance
        if distance < min_distance:
            min_distance = distance
    return min_distance


def get_min_city_chicken_distance(n, m, city_map):
    house_list = []
    store_list = []
    for i in range(len(city_map)):
        for j in range(len(city_map[0])):
            if city_map[i][j] == 1:
                house_list.append((i, j))
            elif city_map[i][j] == 2:
                store_list.append((i, j))

    # Memoization: [집 idx][치킨집 idx] 별로 거리 기록
    record_distance = [[-1 for _ in range(len(store_list))] for _ in range(len(house_list))]

    # 남길 가게들의 경우의 수
    store_select_cases = list(itertools.combinations([i for i in range(len(store_list))], m))

    # 가게들을 선택할 경우마다 최소 거리
    min_distance_by_case = sys.maxsize

    for store_select in store_select_cases:
        total_distance = 0
        for house_idx in range(len(house_list)):
            total_distance += find_closest_distance(house_idx, house_list, store_select, store_list, record_distance)
        if total_distance < min_distance_by_case:
            min_distance_by_case = total_distance
        # print("Case: ", store_select)
        # print("Total:", total_distance)
        # print()

    return min_distance_by_case


# 출력
start = time.time()
print(get_min_city_chicken_distance(n, m, city_map))
print("Time:", start - time.time())
