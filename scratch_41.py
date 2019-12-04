import math
#
# def fact(n):
#     if n == 0 or n== 1:
#         return 1
#     else:
#         return n*fact(n-1)
# for _ in range(0,int(input())):
#     d = int(input())
#     jollly = int(input())
#     result = 2* fact(d) // fact(d-jollly)
#     print(result)

M = 1000000007
for _ in range(0, int(input())):
    d = int(input())
    jolly = int(input())
    N = d- (d - jolly)
    answer = math.factorial(d) // math.factorial(d-jolly)
    print(2 * answer)
