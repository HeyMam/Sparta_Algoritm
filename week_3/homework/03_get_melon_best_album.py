genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


# genres = ["classic", "classic", "classic", "pop"]
# plays = [500, 150, 800, 50]


# [노래 Index, 플레이수] 를 리스트로 저장
class LinkedTuple:
    __items = []  # ?? __init__ 에서 초기화 안하면 static 변수 인건가요?? ㄷㄷ
    __size = 0
    __sum = 0

    def __init__(self):
        self.__items = []
        return

    def add_with_value_sort(self, index, value):
        self.__items.append((index, value))
        self.__sum += value
        self.__size += 1

        length = self.__size

        # 추가하면서 바로 정렬 (value 기준)
        for i in range(length - 1):
            # 비교 대상 Item > 마지막 삽입한 Item
            if self.__items[i][1] < self.__items[length - 1][1]:
                self.__items[i], self.__items[i + 1:length] = self.__items[length - 1], self.__items[i:length - 1]
            break

        return

    def get(self, key):
        for i in range(len(self.__items)):
            if key == self.__items[i][0]:
                return self.__items[i]
        return None

    def get_sorted_by_value(self, count):
        last = count
        if last > len(self.__items):
            last = len(self.__items)
        return self.__items[:last]

    def get_sum(self):
        return self.__sum

    def print(self):
        if self.__size <= 0:
            print("[]")
            return

        print("[", end='')
        for i in range(len(self.__items)):
            print(self.__items[i], sep='', end=' ')
        print("\b] sum:", self.__sum)
        return


# [장르 이름, 장르별 LinkedTuple] 를 리스트로 저장
class LinkedDic:
    __items = []
    __category_size = 0

    def __init__(self):
        self.__items = []
        return

    def add_with_sort_by_value(self, category, idx, value):
        exist_tuple = self.get(category)

        if exist_tuple is None:
            new_tuple = LinkedTuple()
            new_tuple.add_with_value_sort(idx, value)
            # new_tuple.print()
            self.__items.append((category, new_tuple))
            self.__category_size += 1
        else:
            exist_tuple.add_with_value_sort(idx, value)
            # exist_tuple.print()

        # 추가하면서 바로 정렬 (sum 기준)
        length = len(self.__items)
        for i in range(length - 1):
            # 비교 대상 Item > 마지막 삽입한 Item
            if self.__items[i][1].get_sum() < self.__items[length - 1][1].get_sum():
                self.__items[i], self.__items[i + 1:length] = self.__items[length - 1], self.__items[i:length - 1]
            break

        return

    def get(self, category):
        for k, v in self.__items:
            if category == k:
                return v
        return None

    def get_key_sorted_by_sum(self, count):
        best_album_index = [0] * self.__category_size * count
        current = 0
        for genre in self.__items:
            for play in genre[1].get_sorted_by_value(count):
                best_album_index[current] = play[0]
                current += 1

        return best_album_index


# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]

# 모두 다음과 같이 저장된다.
# Category    [Idx, Value] [Idx, Value] [Idx, Value]
# [classic]   [3, 800] [0, 500] [2, 150]      sum: 1450
# [pop]       [4, 600] [1, 2500]              sum: 3100


def get_melon_best_album(genre_array, play_array):
    # 장르별로 노래 저장
    list_per_genre = LinkedDic()

    # 내부에서 바로 정렬하면서 저장
    for i in range(len(genre_array)):
        list_per_genre.add_with_sort_by_value(genre_array[i], i, play_array[i])

    # 각 장르별로 2곡씩 노래의 Index 저장
    best_album = list_per_genre.get_key_sorted_by_sum(2)

    return best_album


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
