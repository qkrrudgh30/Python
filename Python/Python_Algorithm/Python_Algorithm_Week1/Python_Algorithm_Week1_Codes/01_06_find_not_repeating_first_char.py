input = "abacabade"


def find_not_repeating_character(string):
    occ = [0] * 26

    for item in string:
        if item.isalpha():
            occ[ord(item) - ord('a')] += 1

    alpha = []
    for i in range(0, 26):
        if occ[i] == 1:
            alpha.append(chr(i + ord('a')))

    for ch in string:
        if ch in alpha:
            return ch

    return "_"


result = find_not_repeating_character(input)
print(result)