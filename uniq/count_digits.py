"""
Write a program to count the number of digits in a given number
"""

def count_digits(number: int) -> int:
    counter: int = 0
    while number != 0:
        number //= 10 # floor division
        counter += 1
    return counter


if __name__ == '__main__':
    number: int = int(input("Enter a number: "))
    result: str = count_digits(number)
    print(f'There are {result} digits in {number}')
