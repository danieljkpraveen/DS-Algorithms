def search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    item = 5
    index = search(list, item)
    print(f"ITEM {list[index]} AT INDEX: {index}")