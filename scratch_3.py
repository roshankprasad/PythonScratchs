
string = "abracadabra"
# print(string.capitalize())
# print(string.upper())
# print(string.islower())
# print(string.casefold())
# # print(string.index('d'))
# a = -20.788
# print(abs(a))
# print(round(a))
# a = input("enter a number")
# b = input("enter 2nd number")
# c = int(a) + int (b);
# print(c)
# print(a+b)
# print(type(int(a+b)))
# z = int(a+b) + int(a+b)
# print(z)
#
#
# def sqr(x) :
#     return x*x;
# sqr(4)
# print(sqr(25))
#
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return (n * fact(n-1))
#
# n1 = int(input("input a number"))
# n = int(n1)
# print(fact(n))
# print("the end")
#
# number = input("enter a number")
# num = int(number)
# if num % 2 == 0 :
#     print(num, "is even")
# else:
#     print(num, " num is odd")

def fact(num):
    fac = 1
    i = 1
    while i <= num:
	    fac = fac * i
	    i = i + 1
    return fac

n = 23
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("The factorial of 23 is : ", end="")
print(fact)