#  Given an array of integers, determine whether the array is monotonic or not.
"""An array A is monotone increasing if for all i <= j, A[i] <= A[j]. An array A is monotone 
decreasing if for all i <= j, A[i] >= A[j].
"""


def find_monotone(array):
    #  The all() function returns True if all items in an iterable are true, otherwise it returns False. 
    return all(array[i] <= array[i+1] for i in range(len(array) -1)) or all(array[i] >= array[i+1] for i in range(len(array) -1))


if __name__ == '__main__':
    input_array = [6, 5, 4, 4]
    print(find_monotone(input_array))

# __________________ o(n+m) complexity__________________
