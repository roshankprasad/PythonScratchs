# print("Line Start:")
# output:
# 1
# 21
# 321
# 4321
# 54321
# 654321
# 7654321
# 87654321

def fun(n):
    if n == 0 :
        return n
    else:
        return n*pow(10,n-1)+fun(n-1)
for i in range(1,9):
    print(fun(i))

