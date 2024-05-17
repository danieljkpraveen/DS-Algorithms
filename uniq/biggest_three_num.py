"""
Program to find the biggest of three numbers
"""

def find_biggest(num1: int, num2: int, num3: int) -> str:
    biggest: int = 0

    if num1>num2 and num1>num3:
        biggest = num1
    elif num2>num1 and num2>num3:
        biggest = num2
    else:
        biggest = num3

    return f'Biggest of {num1}, {num2}, {num3} is {biggest}'


if __name__ == '__main__':
    num1: int = int(input("Enter 1st number: "))
    num2: int = int(input("Enter 2nd number: "))
    num3: int = int(input("Enter 3rd number: "))
    result: str = find_biggest(num1, num2, num3)
    print(result)
