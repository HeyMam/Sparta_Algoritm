shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


# 단일 품목 검사
def is_available(menus, find):
    first = 0
    last = len(menus) - 1
    while first <= last:
        middle = (first + last) // 2
        if menus[middle] > find:  # find 가 왼쪽에 있음
            last = middle - 1
        elif menus[middle] < find:  # find 가 오른쪽에 있음
            first = middle + 1
        else:
            return True
    return False


def is_available_to_order(menus, orders):
    menus.sort()
    for order in orders:
        if not is_available(menus, order):
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
