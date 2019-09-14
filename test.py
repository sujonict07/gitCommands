def palindrome_index(input_str, index):
    first = index
    last = index
    while (first > 0 and last < len(input_str) - 1 and input_str[first - 1] == input_str[last + 1]):
        first -= 1
        last += 1
    # print(input_str[first:last + 1])
    return input_str[first:last + 1]


def longest_palindrome(input_str):
    best_half_length = 0
    best_index = 0
    index = 0
    while index < len(input_str) - best_half_length:
        palindrome = palindrome_index(input_str, index)
        half_length = (len(palindrome) -1) / 2
        if half_length > best_half_length:
            best_half_length = half_length
            best_index = index
        index += 1
    return palindrome_index(input_str, best_index)


if __name__ == "__main__":
    print(longest_palindrome("1221"))
