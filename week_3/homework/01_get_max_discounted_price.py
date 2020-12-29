shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def ascending(lt, rt):
    return lt < rt


def descending(lt, rt):
    return lt > rt


def merge(left, right, func):
    merge_array = [0] * (len(left) + len(right))
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if func(left[i], right[j]):
            merge_array[i + j] = left[i]
            i += 1
        else:
            merge_array[i + j] = right[j]
            j += 1
        if not i < len(left):
            merge_array[i + j:] = right[j:len(right)]
            break
        if not j < len(right):
            merge_array[i + j:] = left[i:len(right)]
            break
    return merge_array


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])

    return merge(left_array, right_array, descending)


def get_max_discounted_price(prices, coupons):
    prices = merge_sort(prices)
    coupons = merge_sort(coupons)

    total = 0
    for i in range(len(prices)):
        if i < len(coupons):
            total += (prices[i] * (100 - coupons[i])) / 100
        else:
            total += prices[i]

    return total


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
