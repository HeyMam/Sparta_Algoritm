from collections import deque

# 보드의 행/열 크기: 3 ~ 10
# . 빈칸
# # 벽
# O 구멍
# R 빨간 구슬
# B 파란 구슬

# 10번 이하로 움직여서 '빨간 구술만' 빼낼 수 있는지 반환하라

# game_map = [
#     ["#", "#", "#", "#", "#"],
#     ["#", ".", ".", "B", "#"],
#     ["#", ".", "#", ".", "#"],
#     ["#", "R", "O", ".", "#"],
#     ["#", "#", "#", "#", "#"],
# ]  # -> True를 반환해야 한다.

game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "R", "#", ".", ".", ".", "#", "#", "B", "#"],
    ["#", ".", ".", ".", "#", ".", "#", "#", ".", "#"],
    ["#", "#", "#", "#", "#", ".", "#", "#", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
    ["#", ".", "#", "#", "#", "#", "#", "#", ".", "#"],
    ["#", ".", "#", ".", ".", ".", ".", "#", ".", "#"],
    ["#", ".", "#", ".", "#", ".", "#", ".", ".", "#"],
    ["#", ".", ".", ".", "#", ".", "O", "#", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]  # -> False 를 반환해야 한다

#    남, 동, 북, 서
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def is_available_to_take_out_only_red_marble(g_map):
    # 빨간공의 행/열, 파란공의 행/열 필요
    queue = deque()

    current_pos = [0] * 4

    # 첫 시작 위치 넣기
    for i in range(len(g_map)):
        for j in range(len(g_map[i])):
            if g_map[i][j] == "R":
                current_pos[0], current_pos[1] = i, j
            elif g_map[i][j] == "B":
                current_pos[2], current_pos[3] = i, j
    queue.append(current_pos)

    # 게임 시작
    turn = 0
    while turn < 10:
        turn += 1
        print("Turn:", turn)

        # 이전 위치들 순환
        for _ in range(len(queue)):
            prev_pos = queue.popleft()

            # 파란공 다음 위치
            # 동 남 서 북
            for i in range(4):
                # 파란공
                tile = g_map[prev_pos[2] + dr[i]][prev_pos[3] + dc[i]]
                if tile == "O":  # 실패
                    continue
                elif tile == "#":  # 파란공 움직이지 않음
                    current_pos[2], current_pos[3] = prev_pos[2], prev_pos[3]
                else:
                    current_pos[2], current_pos[3] = prev_pos[2] + dr[i], prev_pos[3] + dc[i]
                # 빨간공
                tile = g_map[prev_pos[0] + dr[i]][prev_pos[1] + dc[i]]
                if tile == "O":  # 성공
                    return True
                elif tile == "#":  # 빨간공 움직이지 않음
                    current_pos[0], current_pos[1] = prev_pos[0], prev_pos[1]
                else:
                    current_pos[0], current_pos[1] = prev_pos[0] + dr[i], prev_pos[1] + dc[i]
                # 새로운 위치 삽입
                queue.append(current_pos)

    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다
