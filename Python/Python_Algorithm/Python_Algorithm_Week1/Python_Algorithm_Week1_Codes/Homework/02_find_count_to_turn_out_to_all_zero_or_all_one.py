input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    start = '0'
    count0 = 0
    count1 = 0

    for item in string:
        if start != item:
            count0 += 1
            start = item

    start = '1'
    for item in string:
        if start != item:
            count1 += 1
            start = item

    if count0 < count1:
        return count0 - 1
    else:
        return count1 - 1


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)