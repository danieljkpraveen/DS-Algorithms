"""Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of 
the non-zero elements.
"""

#  move zeros to end of list
def move_end(num_list):
    for n in num_list:
        if 0 in num_list:
            num_list.remove(0)
            num_list.append(0)
    return num_list

# move zeros to beginning of list
def move_start(num_list):
    frequency = 0
    for n in num_list:
        if 0 in num_list:
            num_list.remove(0)
            frequency += 1
    for f in range(frequency):
        num_list.insert(0, 0)
    return num_list


if __name__ == '__main__':
    num_list = [0, 1, 0, 3, 12]
    print(move_end(num_list))
    print(move_start(num_list))