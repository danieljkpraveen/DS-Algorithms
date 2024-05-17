"""
Program to find if a given year is a leap year
"""

def calc_leap(year: str) -> str:
    leap_year: bool = False

    if year.endswith('00'):
        year: int = int(year)
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False

    else:
        year: int = int(year)
        if year % 4 == 0:
            leap_year = True
        else:
            leap_year = False

    if leap_year:
        return f'{year} is a leap year'
    return f'{year} is not a leap year'


if __name__ == '__main__':
    year: str = input("Enter year: ")
    result: str = calc_leap(year)
    print(result)
