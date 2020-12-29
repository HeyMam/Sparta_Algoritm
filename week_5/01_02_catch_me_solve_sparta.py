from collections import deque
import time

c = 11
b = 2


# 브라운이 코니를 잡아야 한다 (b -> c)
# 브라운: 현재 위치에서 -1, +1, *2
# 코니: 이전 속도 + 1

# sol.
# 1. 브라운이든 코니든 누가 먼저 이동했든 중요하지 않다. 위치만 일치하면 된다.
# 2. 큐의 용도는 꺼낸 데이터로 확장된 경우의 수를 다시 넣는데에도 유용하다.
# 3. 이동 변화가 BFS 탐색처럼 펼쳐지는 녀석부터 어떻게 저장하고 다음에 비교할지 고려하자.

# Line 풀이. (k-2 의 해가 k 에 포함되어 있다고 가정하고 풀이하고 있다)
# (-1 -> +1, +1 -> -1 이렇게 이동할 수 있기 때문에 k-2 번째 이동 위치가 k 번째에 포함된다)
# https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test/

def catch_me(cony_loc, brown_loc):
    current_time = 0
    queue = deque()
    queue.append(brown_loc)
    visited = [{} for _ in range(200001)]  # visited[위치][시간] (0.8 mb)
    visited[brown_loc][current_time] = True

    # 0 - 1 - 2     0 = {2: True}
    # 2   1   0     1 = {1: True}
    #     3   2     2 = {0: True, 2: True}
    #     4   3     3 = {1: True, 2: True}
    #         4     4 = {1: True, 2: True}
    #         8     5 = ...

    while True:
        cony_loc += current_time

        if cony_loc > 200000:
            return -1

        if current_time in visited[cony_loc]:
            return current_time

        for i in range(len(queue)):
            current_position = queue.popleft()  # 브라운 위치
            next_time = current_time + 1

            new_position = current_position - 1
            if new_position >= 0:
                queue.append(new_position)
                visited[new_position][next_time] = True

            new_position = current_position + 1
            if new_position <= 200000 and next_time not in visited[new_position]:
                queue.append(new_position)
                visited[new_position][next_time] = True

            new_position = current_position * 2
            if new_position <= 200000 and next_time not in visited[new_position]:
                queue.append(new_position)
                visited[new_position][next_time] = True

        current_time += 1

    return -1


start = time.time()
print(catch_me(c, b))  # 5가 나와야 합니다!
print("time :", '%.6f' % (time.time() - start))
