from collections import deque
import time

c = 11
b = 2


# 브라운이 코니를 잡아야 한다 (b -> c)
# 브라운: 현재 위치에서 -1, +1, *2
# 코니: 이전 속도 + 1

def check_catch(time_count, cony_current, brown_start):
    if time_count == 0:
        return cony_current == brown_start

    time_count -= 1

    # return check_catch(time_count, cony_current, {brown_start + 1, brown_start - 1, brown_start * 2})
    return check_catch(time_count, cony_current, brown_start + 1) or \
           check_catch(time_count, cony_current, brown_start - 1) or \
           check_catch(time_count, cony_current, brown_start * 2)



def catch_me(cony_loc, brown_loc):
    time_count = 0

    # print(check_catch(5, 26, 2))

    while True:

        if cony_loc > 200000:
            break

        time_count += 1
        cony_loc += time_count

        if check_catch(time_count, cony_loc, brown_loc):
            break

    return time_count


start = time.time()
print(catch_me(c, b))  # 5가 나와야 합니다!
print("time :", '%.6f' % (time.time() - start))