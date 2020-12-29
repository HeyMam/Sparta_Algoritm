current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

BLOCK_EMPTY = 0
BLOCK_WALL = 1
BLOCK_CLEANED = 2


class RobotVacuum:
    row = -1  # 현재 위치하는 행
    col = -1  # 현재 위치하는 열
    _dir = -1  # 현재 방향
    cln = 0  # 청소한 블록 수
    room_map = None

    def __init__(self, r, c, d, room_map):
        self.row = r
        self.col = c
        self._dir = d
        self.room_map = room_map

    def rotate(self):
        if self._dir > 0:
            self._dir -= 1
        else:
            self._dir = 3

    def rotate_to(self, d):
        self._dir = d

    def forward(self):
        if self._dir == 0:
            self.row -= 1
        elif self._dir == 1:
            self.col += 1
        elif self._dir == 2:
            self.row += 1
        elif self._dir == 3:
            self.col -= 1

    def backward(self):
        if self._dir == 0:
            self.row += 1
        elif self._dir == 1:
            self.col -= 1
        elif self._dir == 2:
            self.row -= 1
        elif self._dir == 3:
            self.col += 1

    def get_next_dir(self, d):
        if d > 0:
            d -= 1
        else:
            d = 3
        return d

    # 매개변수 방향의 뒤쪽 방향을 반환한다
    def get_back_dir(self, d):
        d = self.get_next_dir(d)
        d = self.get_next_dir(d)
        return d

    # r, c 위치에서 d 방향으로 한 칸 이동한 뒤 위치를 반환한다
    def get_block_by_dir(self, d, r, c):
        if d == 0:
            r -= 1
        elif d == 1:
            c += 1
        elif d == 2:
            r += 1
        elif d == 3:
            c -= 1
        return r, c

    # r, c 위치의 속성(비어있는지, 벽인지, 청소했는지)을 반환한다
    def get_block_prop(self, r, c):
        return self.room_map[r][c]

    def clean_current_block(self):
        if self.room_map[self.row][self.col] == BLOCK_EMPTY:
            self.room_map[self.row][self.col] = BLOCK_CLEANED
            self.cln += 1

    def print_map(self):
        print("Current Clean:", self.cln)
        for i in range(len(self.room_map)):
            for j in range(len(self.room_map[i])):
                print(self.room_map[i][j], end=' ')
            print()
        print()

    def start_clean(self):

        while True:
            # 현재 위치 청소
            self.clean_current_block()

            # 왼쪽 탐색 1
            search_dir = self.get_next_dir(self._dir)
            search_r, search_c = self.get_block_by_dir(search_dir, self.row, self.col)
            if self.get_block_prop(search_r, search_c) == BLOCK_EMPTY:
                self.rotate_to(search_dir)
                self.forward()
                continue

            # 왼쪽 탐색 2
            search_dir = self.get_next_dir(search_dir)
            search_r, search_c = self.get_block_by_dir(search_dir, self.row, self.col)
            if self.get_block_prop(search_r, search_c) == BLOCK_EMPTY:
                self.rotate_to(search_dir)
                self.forward()
                continue

            # 왼쪽 탐색 3
            search_dir = self.get_next_dir(search_dir)
            search_r, search_c = self.get_block_by_dir(search_dir, self.row, self.col)
            if self.get_block_prop(search_r, search_c) == BLOCK_EMPTY:
                self.rotate_to(search_dir)
                self.forward()
                continue

            # 왼쪽 탐색 4
            search_dir = self.get_next_dir(search_dir)
            search_r, search_c = self.get_block_by_dir(search_dir, self.row, self.col)
            if self.get_block_prop(search_r, search_c) == BLOCK_EMPTY:
                self.rotate_to(search_dir)
                self.forward()
                continue

            # 후진 확인
            search_dir = self.get_back_dir(self._dir)
            search_r, search_c = self.get_block_by_dir(search_dir, self.row, self.col)

            # 뒤쪽 방향이 벽이라면 청소 종료
            if self.get_block_prop(search_r, search_c) == BLOCK_WALL:
                break
            # 뒤쪽 방향이 청소는 했지만 비었다면 후진
            else:
                self.backward()

        return self.cln


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    robot_vacuum = RobotVacuum(r, c, d, room_map)

    return robot_vacuum.start_clean()


# 57 이 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
