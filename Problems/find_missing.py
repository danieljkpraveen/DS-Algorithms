""" Given an array of numbers find the missing least positive number that is divisible by 5
Say array = [7,8,9,10,11]

Output is a number that is not in the array and is divisible by 5
"""


def find_missing(number_list):
    smallest = min(number_list)
    positive_numbers = []
    for i in range(0, smallest):
        if (i % 5 == 0):
            positive_numbers.append(i)
    print(max(positive_numbers))


if __name__ == '__main__':
    number_list = [21, 22, 23, 24, 25]
    find_missing(number_list)