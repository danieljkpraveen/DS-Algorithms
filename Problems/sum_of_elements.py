""" You are given an array of positive integers and you need to find the sum of the elements at these indices are
divisible by the number.

example:
arr=[1,2,3,4,5]
d=2
solution(arr,d)=6
(1,2,3) , sum is 6 , which is divisible by 2
(1,2,5), sum is 8 , which is divisible by 2
(1,3,5) sum is 8, which is divisible by 2
(1,4,5), sum is 10 which is divisible by 2
(2,3,5), sum is 10 which is divisible by 2
(3,4,5), sum is 12 which is divisible by 2
"""


def find_sum(number_list, divisor):
    divisibles = []
    copy_indexes = []
    for i in range(len(number_list)):
        for j in range(len(number_list)):
            for k in range(len(number_list)):
                sum = number_list[i] + number_list[j] + number_list[k]
                if (sum % divisor == 0):
                        divisibles.append([number_list[i], number_list[j], number_list[k]])
    for i in range(len(divisibles)):
        for j in range(1, len(divisibles)):
            if (divisibles[i] == divisibles[j][::-1]):
                copy_indexes.append(j)
    for i in copy_indexes:
        if i < len(divisibles):
            divisibles.pop(i)
    print(divisibles, len(divisibles))


if __name__ == '__main__':
    number_list = [1, 2, 3, 4, 5]
    divisor = 2
    find_sum(number_list, divisor)

