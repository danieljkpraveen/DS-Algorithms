"""
Calculate the sum of digits of a given number
"""

def calculate_sum(number: str) -> str:
    if not number.isdigit():
        return f'Invalid input'
    else:
        sum: int = 0
        for digit in number:
            sum = sum + int(digit)
        return f'Sum of {number} is {sum}'


if __name__ == '__main__':
    number: str = input("Enter a number: ")
    result: str = calculate_sum(number)
    print(result)
