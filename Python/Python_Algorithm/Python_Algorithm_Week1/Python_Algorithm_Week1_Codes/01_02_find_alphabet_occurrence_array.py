def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for ch in string:
        if ch.isalpha():
            alphabet_occurrence_array[ord(ch) - ord('a')] = alphabet_occurrence_array[ord(ch) - ord('a')] + 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))