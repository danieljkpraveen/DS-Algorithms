"""
Reverse a given string
"""

# using for loop
def reverse_string(word: str) -> str:
    if word == '':
        return "Invalid input"
    else:
        reversed_word: str = ''
        for character in word:
            reversed_word = character + reversed_word
        return f"reversed word is {reversed_word}"


# using slicing
# def reverse_string(word: str) -> str:
#     if word == '':
#         return "Invalid input"
#     else:
#         reversed_word = word[::-1]
#         return f"reversed word is {reversed_word}"


if __name__ == '__main__':
    word = input("Enter a string: ")
    result: str = reverse_string(word)
    print(result)
