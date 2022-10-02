from sys import argv
from enum import Enum


def check():
    year, month, day, hour, second, minute = (1 for i in range(6))
    if 1900 < year < 2100 and 1 <= month <= 12 \
            and 1 <= day <= 31 and 0 <= hour < 24 \
            and 0 <= minute < 60 and 0 <= second < 60:  # Looks like a valid date
        return 1
    else:
        print("Works")


class Shake():
    VANILLA = 7
    CHOCOLATE = 4
    COOKIES = 9
    MINT = 3

    def __iter__(self):


print(Shake())

# for shake in (Shake):
#     print(shake)
