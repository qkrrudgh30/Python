input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    occurancy = [0] * 26
    max = occurancy[0]
    max_i = 0
    i = 0

    for ch in string:
        if (ch.isalpha()):
            occurancy[ord(ch) - ord('a')] += 1

    for item in occurancy:
        if max < item:
            max = item
            max_i = i + ord('a')

        i += 1

    return chr(max_i)


result = find_max_occurred_alphabet(input)
print(result)