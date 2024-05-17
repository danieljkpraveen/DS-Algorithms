"""
Program to find the biggest of two numbers
"""

def find_biggest(num1: int, num2: int) -> str:
    biggest: int = 0
    biggest = (num1 if num1>num2 else num2)
    return f'Biggest of {num1}, {num2} is {biggest}'


if __name__ == '__main__':
    num1: int = int(input("Enter 1st number: "))
    num2: int = int(input("Enter 2nd number: "))
    result: str = find_biggest(num1, num2)
    print(result)
