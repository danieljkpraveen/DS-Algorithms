"""Given an array containing None values fill in the None values with most recent 
non None value in the array
"""


def fill_none(array):
    valid = 0
    filled = []
    for a in array:
        if a is not None:
            filled.append(a)
            valid = a
        else:
            filled.append(valid)
    return filled


if __name__ == '__main__':
    array = [1, None, 2, 3, None, None, 5, None]
    print(fill_none(array))

# __________________ o(n) complexity__________________