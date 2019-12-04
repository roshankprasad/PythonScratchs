#
# def is_palindrome(string):
#     lst = list(string)
#     rlst = [char for char in lst]
#     rlst.reverse()
#     if lst == rlst:
#         #print("YES")
#         return 1
#     else:
#         #print("NO")
#         return 0
#
# if((is_palindrome(input())) == 1):
#     print("YES")
# else:
#     print("NO")

# string = "Roshan"
# lst = list(string)
# rlst = [ch for ch in lst ]
# rlst.reverse()
# print(lst)
# print(rlst)
#
# lst = []
# testcases = int(input())
# for _ in range(0,testcases):
#     lst.append(int(input()))
# print(lst)
#
# seatNum = int(input())
# #print(seatNum)
# divby3 = int(seatNum/3)
# modby3 = (seatNum % 3)
#
# print("divby3=",divby3)
# print("modby3=",modby3)
# seatBerth =''
# #if seatNum > divby3*3:
# if modby3>0 :
#     compartment =divby3+1
#     print("compartment",compartment)
# else:
#     compartment = divby3;
#     print("compartment",compartment)
# if compartment % 2 == 0:
#     if modby3 ==1 :
#         seatBerth = 'AS'
#     elif modby3 ==2 :
#         seatBerth = 'MS'
#     elif modby3 ==0 :
#         seatBerth = 'WS'
# else:
#     if modby3 ==1 :
#         seatBerth = 'WS'
#     elif modby3 ==2 :
#         seatBerth = 'MS'
#     elif modby3 ==0 :
#         seatBerth = 'AS'
# print(seatBerth)
#
# # if (divby3 % 2 == 0):
# #     print("even",(seatNum+modby3))
# #print(int((divby3) - (divby3+modby3)/3))
# # oppositeSeat = 0
# # if compartment % 4 == 0 :
# #     oppositeSeat = (compartment-4)*3 + modby3+1;
# # print(oppositeSeat)
#
# # if compartment% 4 == 0:
# #     print( ((compartment/4)- 1 )*4 +1)
#
# if compartment % 4 ==0:
#     print(seatNum-11)
# else:
#     print(seatNum+11)


#-------------------------
seatNum = int(input())
divby3 = int(seatNum/3)
modby3 = (seatNum % 3)
#print("divby3=",divby3)
#print("modby3=",modby3)
seatBerth =''
if modby3>0 :
    compartment =divby3+1
    #print("compartment",compartment)
else:
    compartment = divby3;
    #print("compartment",compartment)
#
# if compartment % 2 == 0:
#     if modby3 ==1 :
#         seatBerth = 'AS'
#     elif modby3 ==2 :
#         seatBerth = 'MS'
#     elif modby3 ==0 :
#         seatBerth = 'WS'
# else:
#     if modby3 ==1 :
#         seatBerth = 'WS'
#     elif modby3 ==2 :
#         seatBerth = 'MS'
#     elif modby3 ==0 :
#         seatBerth = 'AS'
# #print(seatBerth)

# if compartment % 4 ==0:
#     print(seatNum-11)
# else:
#     print(seatNum+11)
oppositeCompartment = 0
if compartment%4 == 1 :
        oppositeCompartment = compartment +3
elif compartment % 4 == 2 :
        oppositeCompartment = compartment + 1
elif compartment%4 == 3:
    oppositeCompartment = compartment -1
elif compartment % 4 == 0:
    oppositeCompartment = compartment -3
#print("oppositeCompartment", oppositeCompartment)

num = (compartment-1)*3
#print(num)
oppositeSeat = oppositeCompartment*3 -(seatNum-num)+1

if oppositeSeat % 2 == 0:
    if modby3 ==1 :
        seatBerth = 'AS'
    elif modby3 ==2 :
        seatBerth = 'MS'
    elif modby3 ==0 :
        seatBerth = 'WS'
else:
    if modby3 ==1 :
        seatBerth = 'WS'
    elif modby3 ==2 :
        seatBerth = 'MS'
    elif modby3 ==0 :
        seatBerth = 'AS'
print(oppositeSeat,seatBerth)