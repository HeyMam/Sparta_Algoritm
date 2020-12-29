input_ex = 20


# 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오
# 정수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.


def find_prime_list_under_number(number):

    prime_list = []

    for i in range(2, number):

        is_prime = True

        for prime in prime_list:
            if i % prime == 0:
                is_prime = False
                break

        if is_prime:
            prime_list.append(i)

    return prime_list


result = find_prime_list_under_number(input_ex)
print(result)