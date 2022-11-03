"""______________________________________Reverse number______________________________________
"""


def reverse_integer(number):
    #  function to reverse number and store it in a list
    reversed_list = []
    n = len(number)
    if number.startswith('-'):
        print('negative number')
        reversed_list.append(number[0])
        for i in range(n, 1, -1):
            reversed_list.append(number[i-1])
        print(concat_number(reversed_list))
    else:
        print('positive number')
        for i in range(n, 0, -1):
            reversed_list.append(number[i-1])
        print(concat_number(reversed_list))

def concat_number(num_list):
    #  function to convert a list of numbers of type string to type integer
    s = [integer for integer in num_list]
    num_string = "".join(s)
    reversed_number = int(num_string)
    return reversed_number


"""______________________________________Reverse string______________________________________
"""


def reverse_string(input_string):
    reversed_list = []
    n = len(input_string)
    for i in range(n, 0, -1):
        reversed_list.append(input_string[i-1])
    print(list_to_str(reversed_list))

def list_to_str(string_list):
    s = [item for item in string_list]
    reversed_string = "".join(s)
    return reversed_string

if __name__ == '__main__':
    """number = input("Enter number: ")
    reverse_integer(number)"""
    input_string = input("Enter string: ")
    reverse_string(input_string)