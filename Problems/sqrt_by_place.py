""" Given a number, perform sum of square root by place until it returns 1
Say n = 19
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Output is 1
"""


def calc_one(n):
    n = str(n)
    output = 0
    temp = 0
    for i in range(len(n)):
        squared = pow(int(n[i]), 2)
        output += squared
    while (output != 1):
        output = str(output)
        for i in range(len(output)):
            squared = pow(int(output[i]), 2)
            temp += squared
        output = temp
        temp = 0
    print(output)


if __name__ == '__main__':
    n = 19
    calc_one(n)