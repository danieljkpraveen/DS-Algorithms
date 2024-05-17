"""
Program to check if a given number is a prime number
"""

def check_prime(number: int) -> str:
    if number <= 1:
        return f'{number} is not a prime number'

    elif number <= 3:
        return f'{number} is a prime number'

    elif number%2 == 0 or number%3 == 0:
        return f'{number} is not a prime number'

    i: int = 5
    while i *i <= number:
        if (number % i == 0 \
            or number % (i+2) == 0):
            return f'{number} is not a prime number'
        i+=6
    return f'{number} is a prime number'


if __name__ == '__main__':
    number: int = int(input("Enter number: "))
    result: str = check_prime(number)
    print(result)

"""
How the function works -
Check for numbers less than or equal to 1: The function first checks if the number `n`
is less than or equal to 1. If it is, the function returns `False`, because numbers less
than or equal to 1 are not considered prime numbers.

Check for numbers less than or equal to 3: If `n` is less than or equal to 3, the function
returns `True`. This is because 2 and 3 are prime numbers.

Check for divisibility by 2 or 3: If `n` is divisible by 2 or 3, the function returns `False`.
This is because a prime number is only divisible by 1 and itself, so if `n` is divisible by 2 or 3,
it cannot be prime.

Check for divisibility by numbers in the form 6k ± 1: If none of the above conditions are met,
the function enters a while loop where it checks for divisibility by numbers in the form 6k ± 1,
starting with k = 1 (i.e., i = 5). This is an optimization that checks for divisibility by all
possible prime numbers, as all prime numbers are of the form 6k ± 1. If `n` is divisible by any
of these numbers, the function returns `False`.

Return True if no factors found: If the function has not returned `False` after all these checks,
it means that no factors other than 1 and `n` have been found for `n`. Therefore, `n` must be a
prime number, and the function returns `True`.

This function is efficient because it reduces the number of checks needed to determine if a number
is prime. It only checks divisibility up to the square root of `n`, and within that range, it only
checks numbers of the form 6k ± 1. This significantly reduces the number of iterations needed for large numbers.
"""
