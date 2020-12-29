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

# # Test Case 2
# Answer: 10
n = 5
m = 2

city_map = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2],
]


# # Test Case 4
# # Answer: 32
# n = 5
# m = 1
#
# city_map = [
#     [1, 2, 0, 2, 1],
#     [1, 2, 0, 2, 1],
#     [1, 2, 0, 2, 1],
#     [1, 2, 0, 2, 1],
#     [1, 2, 0, 2, 1],
# ]


# 0: 빈칸
# 1: 집
# 2: 치킨집

# 2 <= N <= 50  - 도시 가로/세로 크기
# 1 <= M <= 13  - 페업 시키지 않을 치킨집 최대 수
# 1 <= 집의 개수 <= 2N
# 치킨 집 최대 M개를 골랐을 때, 치킨 거리의 최솟값 출력하기

def get_min_city_chicken_distance(n, m, city_map):
    chicken_location_list = []
    home_location_list = []
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                home_location_list.append([i, j])
            elif city_map[i][j] == 2:
                chicken_location_list.append([i, j])

    chicken_location_m_combinations = list(itertools.combinations(chicken_location_list, m))
    min_distance_of_m_combinations = sys.maxsize

    for chicken_location_m_combination in chicken_location_m_combinations:
        city_chicken_distance = 0
        for home_r, home_c in home_location_list:
            min_home_chicken_distance = sys.maxsize
            for chicken_location in chicken_location_m_combination:
                min_home_chicken_distance = min(
                    min_home_chicken_distance,
                    abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1])
                )
            city_chicken_distance += min_home_chicken_distance
        min_distance_of_m_combinations = min(
            min_distance_of_m_combinations,
            city_chicken_distance
        )

    return min_distance_of_m_combinations


# 출력
start = time.time()
print(get_min_city_chicken_distance(n, m, city_map))
print("Time:", start - time.time())
