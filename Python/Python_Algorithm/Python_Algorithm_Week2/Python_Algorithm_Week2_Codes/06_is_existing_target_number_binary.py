finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    '''
    i = 0;
    max_i = len(array) - 1
    min_i = 0
    middle_i = (max_i + min_i) // 2

    while True:
        if target == array[middle_i]:
            return True
        elif target <= array[middle_i]:
            min_i = middle_i + 1
        elif array[middle_i] < target:
            max_i = middle_i - 1
    '''
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1

        current_guess = (current_min + current_max) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)

result = is_existing_target_number_binary(34, finding_numbers)
print(result)