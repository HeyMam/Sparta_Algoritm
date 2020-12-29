k = 4  # 말의 개수

TILE_WHITE = 0
TILE_RED = 1
TILE_BLUE = 2

# chess_map = [
#     [0, 0, 2, 0],
#     [0, 0, 1, 0],
#     [0, 0, 1, 2],
#     [0, 2, 0, 0],
# ]
#
# start_horse_location_and_directions = [
#     [1, 0, 0],  # 동
#     [2, 1, 2],  # 북
#     [1, 1, 0],  # 동
#     [3, 0, 1]   # 서
# ]

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]

# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]  # 행
dy = [1, -1, 0, 0]  # 열


def get_reverse_direction(direction):
    direction += 2
    if direction > 3:
        direction -= 4
    return direction


def get_tile_type(r, y, game_map):
    if r < 0 or r > 3 or y < 0 or y > 3:
        return TILE_BLUE
    else:
        return game_map[r][y]


def move_from_tile(node_map, r, y, horse_idx):
    exists = node_map[r][y]
    result = None
    for i in range(len(exists)):
        if exists[i] == horse_idx:
            result = exists[i:]
            node_map[r][y] = exists[:i]
            break
    if len(node_map[r][y]) == 0:
        node_map[r][y] = None
    return result


def move_to_tile(node_map, r, y, news, horses):
    exists = node_map[r][y]
    if exists is not None:
        exists.extend(news)
    else:
        node_map[r][y] = news
    for i in news:
        horses[i][0], horses[i][1] = r, y
    return


def is_game_over(node_map, r, y, horse_count):
    cur = node_map[r][y]
    return cur is not None and len(cur) == horse_count


def print_map(game_map):
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            print(game_map[i][j], end=' ')
        print()
    return


def print_map_and_horses(turn, idx, node_map):
    print("Turn:", turn, ", Idx:", idx)
    for i in range(len(node_map)):
        for j in range(len(node_map[i])):
            print(node_map[i][j], end=' ')
        print()
    print()
    return


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    turn = 0
    node_map = [[None] * len(game_map[i]) for i in range(len(game_map))]

    # 말 위치에 배치
    for i in range(horse_count):
        horse = horse_location_and_directions[i]
        node_map[horse[0]][horse[1]] = [i]

    print_map_and_horses(turn, -1, node_map)

    # 게임 시작
    while turn < 1000:
        # 말 순서대로 진행
        for i in range(horse_count):
            horse = horse_location_and_directions[i]
            d = horse[2]

            # 이동할 칸 위치
            new_r, new_y = horse[0] + dr[d], horse[1] + dy[d]
            tile_type = get_tile_type(new_r, new_y, game_map)

            # 파란색: 뒤 칸 검색
            if tile_type == TILE_BLUE:
                d = get_reverse_direction(d)
                new_r, new_y = horse[0] + dr[d], horse[1] + dy[d]
                tile_type = get_tile_type(new_r, new_y, game_map)

            # 흰색: 이동한 후, 순서대로 쌓는다
            if tile_type == TILE_WHITE:
                group = move_from_tile(node_map, horse[0], horse[1], i)
                move_to_tile(node_map, new_r, new_y, group, horse_location_and_directions)
                if is_game_over(node_map, new_r, new_y, horse_count):
                    return turn
            # 빨간색: 이동한 후, 움직인 말과 위의 말들을 순서를 반대로 바꾼다
            elif tile_type == TILE_RED:
                group = move_from_tile(node_map, horse[0], horse[1], i)
                move_to_tile(node_map, new_r, new_y, list(reversed(group)), horse_location_and_directions)
                if is_game_over(node_map, new_r, new_y, horse_count):
                    return turn
            # 또 파란색: 방향만 바꾼뒤 멈춘다
            elif tile_type == TILE_BLUE:
                horse[2] = d

            print_map_and_horses(turn, i, node_map)

        turn += 1

    return -1


# 2가 반환 되어야합니다
print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))
