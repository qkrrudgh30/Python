input = 20


def find_prime_list_under_number(number):
    list = []

    for i in range(2, number+1):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            list.append(i)


    return list


result = find_prime_list_under_number(input)
print(result)