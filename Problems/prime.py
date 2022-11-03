"""Given k numbers which are less than n, return the set of prime number among them
Note: The task is to write a program to print all Prime numbers in an Interval.
Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""
def prime(n):
    prime_nums = []
    for num in range(n):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
                else:
                    if num not in prime_nums:
                        prime_nums.append(num)
    return prime_nums


if __name__ == '__main__':
    n = 35
    print(prime(n))