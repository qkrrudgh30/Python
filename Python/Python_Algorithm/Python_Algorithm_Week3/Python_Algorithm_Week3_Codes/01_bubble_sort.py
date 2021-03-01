input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    length = len(array)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if array[j + 1] < array[j]:
                array[j], array[j + 1] = array[j + 1], array[j]


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!