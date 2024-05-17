"""
Program to extract the first and last items of a list sequentially
and pair them as tuples.
E.g, 
input: [5, 6, 7, 3, 8, 1, 4, 2]
output: [(5, 2), (6, 4), (7, 1), (3, 8)]
"""

from typing import List

def pair_items(numbers: List[int]):
    low: int = 0
    high: int = len(numbers)-1
    mid: int = low+high//2

    paired_list = []

    while low <= mid:
        paired_list.append((numbers[low], numbers[high]))
        low += 1
        high -= 1

    print(f'Input list: \n{numbers}')
    print(f'List of tuples: \n{paired_list}')


if __name__ == '__main__':
    numbers: List[int] = [5, 6, 7, 3, 8, 1, 4, 2]
    pair_items(numbers)
