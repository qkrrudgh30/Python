input = [3, 5, 6, 1, 2, 4]
input2 = [4, 5, 6, 1, 2, 3]


def is_number_exist(number, array):

    for item in array:
        if number == item:
            return True

    return False


result = is_number_exist(7, input)
print(result)