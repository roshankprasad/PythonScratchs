#
# testcases = int(input())
# for _ in range(0,testcases):
#     lst, lst2 = map(list, input().split(" "))
#     d = {}
#     for element in lst:
#         if element in d.keys():
#             d[element] += 1
#         else:
#             d[element] =1
#     d2 = {}
#     for element in lst2:
#         if element in d2.keys():
#             d2[element] += 1
#         else:
#             d2[element] =1
#     if d == d2:
#         print("YES")
#     else:
#         print("NO")

person = input('Enter your name: ')
print('Hello ', person, '!', sep=' ')