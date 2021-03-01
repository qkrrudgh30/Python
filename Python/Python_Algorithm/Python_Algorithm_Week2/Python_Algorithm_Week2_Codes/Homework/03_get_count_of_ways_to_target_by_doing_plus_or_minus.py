numbers = [1, 1, 1, 1, 1]
target_number = 3

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    if sum(array) == target:
        return 1

    return get_count_of_ways_to_target_by_doing_plus_or_minus(array, target)


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!

f([])