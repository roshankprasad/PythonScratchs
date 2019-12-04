# x = int ( input())
# y = int ( input())
# z = int ( input())
# n = int ( input())
# ar = []
# p = 0
# for i in range ( x + 1 ) :
#     for j in range( y + 1):
#         for k in range(z+1):
#             if i+j+k != n:
#                 ar.append([])
#                 ar[p] = [ i , j ,k]
#                 p+=1
# print(ar)
#
# def runnerupsocre(lst,n):
#     for i in range(n+1):
#         if lst[-i-1] < lst[-i] :
#             return lst[-i-1]
#
# n = int(input())
# lst = [];
# for i in range(n):
#     lst.append(int(input()))
# lst.sort()
# print(lst)
# print(runnerupsocre(lst,n))

# n = int(input())
# integer_list = tuple(map(int, input().split()))
# print(hash(integer_list))
# tup = (1,2)
# print(hash(tup))
# tup2 = (1,4)
# print(hash(tup2))

s = set("hello")
s.add("ros")
print(s)
s.add("tos")
print(s)