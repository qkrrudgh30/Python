finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    current_max = len(numbers)
    current_min = 0
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if target == numbers[current_guess]:
            return True
        elif numbers[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1

        current_guess = (current_min + current_max) // 2

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)