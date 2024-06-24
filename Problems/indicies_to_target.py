"""Given an array and a target, find the indexes of the indices that sum up to the target
"""


def find_sum(num_list, target):
    #  function to find index of indices that sum to target
    checked = {}
    n = len(num_list)
    for i in range(n):
        if target - num_list[i] in checked:
            print(checked[target - num_list[i]], i)
        else:
            checked[num_list[i]] = i


if __name__ == '__main__':
    num_list = [2, 7, 5, 6, 1]
    target = 6
    find_sum(num_list, target)