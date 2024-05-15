"""Given an array containing None values fill in the None values with most recent 
non None value in the array
"""

from typing import List


def fill_none(array: List) -> str:
    valid: int = 0
    filled = []
    for item in array:
        if item is not None:
            filled.append(item)
            valid = item
        else:
            filled.append(valid)
    return f"Filled array is \n{filled}"


if __name__ == '__main__':
    array: List = [1, None, 2, 3, None, None, 5, None]
    result: str = fill_none(array)
    print(result)

# __________________ o(n) complexity__________________