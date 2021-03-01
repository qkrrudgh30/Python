input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)

    for i in range(1, n):    # 첫 번째 원소는 정렬 되어 있다고 생각합니다.
        for j in range(i):
            if array[i - j] < array[i - j - 1]:
                array[i - j], array[i - j - 1] = array[i - j - 1], array[i - j]
            else:
                break

    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!