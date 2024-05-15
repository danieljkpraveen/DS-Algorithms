"""Given a number in it's binary representation, find the longest sequence of zeros
Example: N = 1041 returns 5, binary representation of 1041 is 10000010001 and the longest
binary gap is 5. N is within 1 - 2147483647
"""
from typing import List


def find_gap(number: int) -> str:
    raw_binary: str = bin(number)
    binary_list: List[str] = raw_binary.split('b')
    binary_number: str = str(binary_list[1])
    zero_counter = []
    counter = 0
    for num in binary_number:
        if (num == '0'):
            counter += 1
        elif (num == '1'):
            zero_counter.append(counter)
            counter = 0
    longest_number: int = max(zero_counter)
    return f"The longest sequence of zeros for {number} is {longest_number}"


if __name__ == '__main__':
    number: int = int(input("Enter number: "))
    if number < 1 or number > 2147483647:
        print("number out of range")
    else:
        result = find_gap(number)
        print(result)
