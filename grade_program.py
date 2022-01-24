#!/usr/bin/env python3

# Created by: Logan S
# Created on: Jan. 21, 2022
# This program calculates a student's mark based on their percentage.


def calc_mark(level):
    levels = {
        "R": "{} has a middle percentage of 25%.". format(level),
        "1-": "{} has a middle percentage of 51%.". format(level),
        "1": "{} has a middle percentage of 55%.". format(level),
        "1+": "{} has a middle percentage of 58%.". format(level),
        "2-": "{} has a middle percentage of 61%.". format(level),
        "2": "{} has a middle percentage of 65%.". format(level),
        "2+": "{} has a middle percentage of 68%.". format(level),
        "3-": "{} has a middle percentage of 71.". format(level),
        "3": "{} has a middle percentage of 75%.". format(level),
        "3+": "{} has a middle percentage of 78%.". format(level),
        "4-": "{} has a middle percentage of 83%.". format(level),
        "4": "{} has a middle percentage of 91%.". format(level),
        "4+": "{} has a middle percentage of 95%.". format(level),
        "4++": "{} is 100%!". format(level),
    }
    return levels.get(level, "Error, Try again?")

def main():

    # User input
    user_level = str(input("Enter the number of a level: "))
    print(calc_mark(user_level))


if __name__ == "__main__":
    main()
