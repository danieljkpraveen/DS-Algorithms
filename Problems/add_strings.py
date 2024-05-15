"""Given two non-negative numbers as strings, find their sum 
n1 = '123', n2 = '321', sum = 444
"""

def add_string(num1: str, num2: str) -> str:
    try:
        sum: int = int(num1) + int(num2)
        return f"sum of {num1} and {num2} is {sum}"
    except ValueError:
        return "Invalid input!"


if __name__ == '__main__':
    num1: str = input("Enter num1: ")
    num2: str = input("Enter num2: ")
    result: str = add_string(num1, num2)
    print(result)
