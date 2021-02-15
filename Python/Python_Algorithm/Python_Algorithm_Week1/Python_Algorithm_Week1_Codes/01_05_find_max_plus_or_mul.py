input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    res = 0

    for item in array:
        if item <= 1 or res <= 1:
            res += item
        else :
            res *= item

    return res


result = find_max_plus_or_multiply(input)
print(result)