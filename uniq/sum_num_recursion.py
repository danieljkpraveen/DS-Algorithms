"""
Calculate the sum of digits of a given number using recursion
"""

def recursive_sum(number: str) -> int:
    if not number:
        return 0
    else:
        return int(number[0]) + int(recursive_sum(number[1:]))
    


if __name__ == '__main__':
    number: str = input("Enter a number: ")
    if not number.isdigit():
        print("Invalid input")
        exit()
    result: int = recursive_sum(number)
    print(f'Sum of {number} is {result}')

"""
Let's say the input is "123":

- The function calls itself with "123".
- Since "123" is not empty, the first digit "1" (converted to integer) is extracted.
- The function recursively calls itself with the remaining digits "23".
- In the recursive call, "23" is not empty, so the first digit "2" is extracted.
- Another recursive call happens with "3".
- Now, "3" is empty, so the base case is reached, and it returns 0.
- The function that called with "3" (step 5) receives 0 and adds the extracted digit "2" (from step 4), returning 2.
- Similarly, the function that called with "23" (step 3) receives 2 and adds the extracted digit "1" (from step 1), returning 3.
- Finally, the initial function receives 3 and returns it as the sum of digits (1 + 2 + 3).
"""
