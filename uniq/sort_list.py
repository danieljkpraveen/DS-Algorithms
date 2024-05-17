"""
Program to sort a list such that the first half is in ascending order
and second half is in descending order.
"""

from typing import List

def sort_items(numbers: List[int]):
    print(f"Input list: \n {numbers}")
    numbers.sort()
    low: int = 0
    high: int = len(numbers)-1
    mid: int = low+high//2

    ascending_list = []
    descending_list = []

    ascending_list = numbers[low:mid+1]
    descending_list = numbers[mid+1:high+1]
    # while low <= mid:
    #     ascending_list.append(numbers[low])
    #     low += 1

    # while high > mid:
    #     descending_list.append(numbers[high])
    #     high -= 1

    print(f"Ascending list: \n{ascending_list}")
    print(f"Descending list: \n{descending_list}")


if __name__ == '__main__':
    numbers: List[int] = [5, 6, 7, 3, 8, 1, 4, 2]
    sort_items(numbers)
