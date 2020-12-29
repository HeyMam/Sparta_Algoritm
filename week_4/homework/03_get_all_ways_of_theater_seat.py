seat_count = 9
vip_seat_array = [4, 7]

EMPTY = -1


# 오래 걸렸던 이유
# 1. "index >= 0" 구문을 "index > 0" 으로 써서 비교 계산 틑림
#    - 심지어 재귀함수 내부라서 찾기 어려움
#    sol. "index >= 0" 구문은 자주 사용하니 익숙해지자
#    sol. 침착하게 결과가 잘못 기록되는 부분 전후로 디버깅하자

def get_number_of_cases(seats, cur):
    total_cases = 0

    # 마지막 좌석까지 체크되면 경우의 수 +1
    if cur >= len(seats):
        print(seats)
        return 1

    # 왼쪽으로 옮겼을 때
    if cur - 1 >= 0 and seats[cur - 1] == EMPTY:
        seats[cur - 1] = cur
        total_cases += get_number_of_cases(seats, cur + 1)
        seats[cur - 1] = -1

    # 제자리일 때
    if seats[cur] == EMPTY:
        seats[cur] = cur
        total_cases += get_number_of_cases(seats, cur + 1)
        seats[cur] = -1

    # 오른쪽으로 옮겼을 때
    if cur + 1 < len(seats) and seats[cur + 1] == EMPTY:
        seats[cur + 1] = cur
        total_cases += get_number_of_cases(seats, cur + 1)
        seats[cur + 1] = -1

    return total_cases


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways_count = 1
    seat_blocks = []
    cases_by_seat_count = {}  # 좌석 개수별 경우의 수 Memoization

    # VIP 좌석을 기준으로 죄석들을 블록으로 구분한다
    normal_seat_len = 0
    for i in range(total_count):
        if i + 1 in fixed_seat_array:
            seat_blocks.append(normal_seat_len)
            normal_seat_len = 0
        else:
            normal_seat_len += 1
    seat_blocks.append(normal_seat_len)

    # VIP 좌석 외의 블록에서 생기는 경우의 수를 서로 곱한다
    for i in range(len(seat_blocks)):
        if seat_blocks[i] not in cases_by_seat_count:
            cases_by_seat_count[i] = get_number_of_cases([-1] * seat_blocks[i], 0)
        all_ways_count *= cases_by_seat_count[i]

    return all_ways_count


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
