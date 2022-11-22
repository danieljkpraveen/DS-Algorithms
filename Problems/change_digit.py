""" You are given a string S, consisting of N digits, that represents a number. You can change at most one digit in the
string to any other digit. How many different numbers divisible by 3 can be obtained in the way?
write afunction:
def solution(S) that, given a a string S of lenght N, return an integers specifying how many numbers divisible by 3 can be
obtained with at most one change of a digit.
Ex:
1.Given S="23", the function should return 7, All numbers divisible by 3 that can be obtained after at most one
change are: "03","21","24","27","33","63" and "93".

2. Given S="0081", the function should return 11. All the numbers divisible by 3 that can be obtained with at most one
change are: "0021","0051","0081","0084","0087","0381","0681","0981","3081","6081" and "9081".

3.Given S="022",the function should return 9. All the numbers divisible by 3 that can be obtained with at most one
change are : "021","021","024","027","042","072","222","522" and "822
"""


def find_divisible(S):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    divisibles = []
    for i in range(len(S)):
        for n in range(len(numbers)):
            temp_num = S.replace(S[i], numbers[n])
            if (int(temp_num) % 3 == 0):
                divisibles.append(temp_num)
    final = []
    for d in divisibles:
        if d not in final:
            final.append(d)
    print(final)


if __name__ == '__main__':
    S = '23'
    find_divisible(S)