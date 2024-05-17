"""
program to check if a given number is odd or even
parity - refers to the property of a number being even or odd
"""

def check_parity(number: int) -> str:
    parity: str = ''

    if number % 2 == 0:
        parity = 'even'
    else:
        parity = 'odd'

    return f'Entered number is {parity}'


if __name__ == '__main__':
    number: int = int(input("Enter a number: "))
    result: str = check_parity(number)
    print(result)
