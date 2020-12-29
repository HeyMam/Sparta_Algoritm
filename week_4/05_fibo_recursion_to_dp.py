input = 20
fibo = [0, 1]


# fibo = [0, 1, 1, 2, 3]

def fibo_recursion(n):
    cur = len(fibo) - 1
    while cur <= n:
        cur += 1
        fibo.append(fibo[cur - 1] + fibo[cur - 2])

    return fibo[n]


print(fibo_recursion(input))  # 6765
