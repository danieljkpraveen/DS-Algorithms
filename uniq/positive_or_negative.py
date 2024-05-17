# program to check if a number is positive or negative

def check_num(number: int) -> str:
    integer_state: str = ''

    if number > 0:
        integer_state = 'positive'
    elif number == 0:
        integer_state = 'zero'
    elif number < 0:
        integer_state = 'negative'

    return f'The entered number is {integer_state}'


if __name__ == '__main__':
    number: int = int(input("Enter a number: "))
    result: str = check_num(number)
    print(result)
