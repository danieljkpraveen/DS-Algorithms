"""Given a number in it's binary representation, find the longest sequence of zeros
Example: N = 1041 returns 5, binary representation of 1041 is 10000010001 and the longest
binary gap is 5. N is within 1 - 2147483647
"""


def find_gap(n):
    raw_binary = bin(n)
    raw_binary = raw_binary.split('b')
    binary_number = str(raw_binary[1])
    zero_counter = []
    counter = 0
    for i in range(len(binary_number)):
        if (binary_number[i] == '0'):
            counter += 1
        elif (binary_number[i] == '1'):
            zero_counter.append(counter)
            counter = 0
    print(max(zero_counter))


if __name__ == '__main__':
    n = int(input("Enter n: "))
    if (n > 0 and
        n <= 2147483647):
        find_gap(n)

