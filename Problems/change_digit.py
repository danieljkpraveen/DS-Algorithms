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


def find_divisible(number: str) -> str:
    divisibles = set()
    for index in range(len(number)):
        for swap in '0123456789':
            swapped_number = int(number[:index] + swap + number[index+1:])
            if swapped_number % 3 == 0:
                divisibles.add(swapped_number)
    return f"divisible numbers are \n{divisibles}"


if __name__ == '__main__':
    number: str = input("Enter number: ")
    result = find_divisible(number)
    print(result)
