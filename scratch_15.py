# # list = []
# # commands = []
# # #for command in range(int(input())):
# #  #   commands.append(input())
# # for command in  range(int(input())):
# #     commands.append(input().rstrip('\n').split())
# #
# # for cmd in commands:
# #     for i in cmd:
# # print(list)
# #
# # slist =  input().rstrip('\n').split()
# # for i in slist:
# #     print(i.capitalize(),end=" ")
#
# s = "hello world"
# lst = s.split()
# for word in lst:
#     print(word.capitalize(),end=" ")

def iseven(nums):
    accum = []
    for num in nums:
        if num%2 ==0 :
            accum.append(num)
    return accum
nums = [3,5,7,9,2,8,4,6]
evens = iseven(nums)
print(evens)

#(lambda x : return x*x)


