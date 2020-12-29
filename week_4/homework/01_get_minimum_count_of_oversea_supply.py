import heapq

ramen_stock = 4  # 4일째에 다 쓰고, 4일째에는 무조건 공급 받아야 한다
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


# 언제, 얼만큼 공급 받는지에 대한 정보
class SupplyInfo:
    date = 0
    supplies = 0

    def __init__(self, date, supplies):
        self.date = date
        self.supplies = supplies

    def __lt__(self, other):
        return self.supplies > other.supplies


# 공급 정보르 가지고서 최소 공급 횟수를 계산해준다
class SupplySchedule:
    stock = 0
    priority_dates = []
    record_dates = []
    last_supply_date = 0

    def __init__(self, stock, dates, supplies):
        self.stock = stock
        for i in range(len(dates)):
            heapq.heappush(self.priority_dates, SupplyInfo(dates[i], supplies[i]))

    # 공급 받아야하는 최소 횟수 구하기 ()
    def get_supply_count(self, recover_date):
        supply_count = 0

        while True:
            get_most_supply = self.__get_most_supply()
            if get_most_supply is None:
                return -1

            self.record_dates.append(get_most_supply)
            supply_count += 1

            if self.last_supply_date + self.stock > recover_date:
                break

        return supply_count

    # 공급을 가장 많이 주는 날 찾기
    def __get_most_supply(self):
        most_supply = None
        temp_supply_info = []

        while True:
            most_supply = heapq.heappop(self.priority_dates)

            # supply 받기전에 재고가 바닥난다면 다른 날을 찾아본다
            if self.stock - most_supply.date < 0:
                temp_supply_info.append(most_supply)
            else:
                for info in temp_supply_info:
                    heapq.heappush(self.priority_dates, info)
                self.stock = self.stock - (most_supply.date - self.last_supply_date) + most_supply.supplies
                self.last_supply_date = most_supply.date
                break

        return most_supply

    def print(self):
        print("Last Supply Date:", self.last_supply_date)
        print("Last Day Stock:", self.stock)
        for i in range(len(self.record_dates)):
            print(i + 1, ":", "Day: ", self.record_dates[i].date, ", Supply: ", self.record_dates[i].supplies)
        print()


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    supply_schedule = SupplySchedule(stock, dates, supplies)
    minimum_count = supply_schedule.get_supply_count(k)
    supply_schedule.print()
    return minimum_count


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
