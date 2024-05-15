"""Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1. 
Note: all the input strings are already lowercase.
"""


def find_unique(input_string):
    frequency = {}
    for letter in input_string:
        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter] += 1
    for letter in input_string:
        if frequency[letter] == 1:
            return f"character {letter} appears {frequency[letter]} time"
    return f"{-1} no unique characters"


if __name__ == '__main__':
    input_string = "bob"
    print(find_unique(input_string))

# __________________ o(n+m) complexity__________________