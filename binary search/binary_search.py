from typing import List


def search(numbers: List[int], query: int) -> str:
    low: int = 0
    high: int = len(numbers)-1

    while low <= high:
        mid: int = (low + high)
        guess: int = numbers[mid]
        if guess == query:
            return f"index of {query} is {mid}"
        if guess > query:
            high = mid - 1
        else:
            low = mid + 1
    return f"{query} not found"

if __name__ == '__main__':

    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    query: int = int(input("Enter a number (1-10): "))
    result = search(numbers, query)
    print(result)
