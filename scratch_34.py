#conject-it.
# N = int(input())
# while N !=1:
#     if N%2 == 0:
#         N=(N//2)
#         print(N)
#     else:
#         N =3*N +1
#         print(N)
# # if N == 1:
# #     print("YES")
# # else:
# #     print("NO")
# print(N)

#
# testcases = int(input())
# number = ""
# for _ in range(0,testcases//2):
#     N = input()
#     number = number + N[0]
# # print(number)
#
# for _ in range(testcases//2,testcases):
#     N = int(input())
#     number = number + str(N%10)
# #print(number)
# if int(number)%11==0 :
#     print("OUI")
# else:
#     print("NO")

testcases = int(input())
inputlst = list(map(str,input().split()))
number = ""
for i in range(0,testcases//2):
    N = inputlst[i]
    number = number + N[0]
# print(number)

for i in range(testcases//2,testcases):
    N = int(inputlst[i])
    number = number + str(N%10)
#print(number)
if int(number)%11==0 :
    print("OUI")
else:
    print("NO")