#isbn problem on hacker rank

# isbn = list(input())
# if len(isbn) == 10:
#     number = 0
#     accum = 1
#     for digit in isbn:
#         number = number + int(digit) * accum
#         accum += 1
#     if number%11 ==0:
#         print("Legal ISBN")
# else:
#     print("Illegal ISBN")

#goki n his breakup problem on hacker rank
    # numberOfPeople = int(input())
    # minimumSkillRequired = int(input())
    # lst = []
    # for _ in range(0,numberOfPeople):
    #     lst.append(int(input()))
    # for skillOfPerson in lst:
    #     if skillOfPerson >= minimumSkillRequired:
    #         print("YES")
    #     else:
    #         print("NO")

#
# i = 0
# lst = []
# last = 0
# while last!=42:
#     lst.append(int(input()))
#     last = lst[i]
#     i += 1
# print(lst)

#break scanning input if 42 comes !
# lst = []
# last = 0
# while last!=42:
#     last = int(input())
#     if last ==42:
#         break
#     lst.append(last)
# print(lst)

# lst =[]
# last_digit = ""
# for _ in range(0,int(input())):
#     lst.append(int(input()))
# for num in lst:
#     last_digit = last_digit + str(num % 10)
# number = int(last_digit)
# if number%10 == 0:
#     print("Yes")
# else:
#     print("No")
#------------------
#
# N = int(input())
# data = [int(x) for x in input().split()]
# last_digit = ""
# for num in data:
#     last_digit = last_digit + str(num % 10)
# number = int(last_digit)
# if number%10 == 0:
#     print("Yes")
# else:
#     print("No")
#please solve the above question once again cuz in it is taking more memory than usual

