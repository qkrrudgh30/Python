input = "abcba"


def is_palindrome(string):
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True

    return is_palindrome(string[1:-1])




print(is_palindrome(input))
print(is_palindrome("tomato"))
print(is_palindrome("소주만병만주소"))