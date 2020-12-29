from collections import deque
import time

c = 11
b = 2


# 브라운이 코니를 잡아야 한다 (b -> c)
# 브라운: 현재 위치에서 -1, +1, *2
# 코니: 이전 속도 + 1

def catch_me(cony_loc, brown_loc):

    return -1


start = time.time()
print(catch_me(c, b))  # 5가 나와야 합니다!
print("time :", '%.6f' % (time.time() - start))
