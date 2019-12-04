# #leap year
# year = int(input())
# def is_leap(year):
#     leap = False
#
#     if year % 4 == 0:
#         if year % 100 == 0 :
#             if year % 400 != 0:
#                 leap = False
#             else:
#                 leap = True
#         else:
#             leap = True
#
#     return leap
#     #
#     # if leap ==False:
#     #     return '13.09.{}'.format(year)
#     # else:
#     #     return '12.09.{}'.format(year)
#
# print(is_leap(year))

# programmer's day problem Hackerrank

year = int(input())
def is_leap(year):
    leap = False
    if 1700 <= year <= 1917:
        print("1st")
        if year%4 == 0:
            leap = True
    else:
        print("2nd")
        if year % 4 == 0:
            if year % 100 == 0 :
                if year % 400 != 0:
                    leap = False
                else:
                    leap = True
            else:
                leap = True

    if leap ==False:
        return '13.09.{}'.format(year)
    else:
        return '12.09.{}'.format(year)

print(is_leap(year))