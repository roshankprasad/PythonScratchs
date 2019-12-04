#
# num1 = list(input())
# num2 = list(input())
#
# sum = 0
# for var in num1:
#     if var not in num2:
#         sum  = sum + int(var)
# print(sum)

for _ in range(0,int(input())):
    word1 = list(input())
    word2 = list(input())
    setlst = set(word1+word2)
    totalLetter = len(word1)+len(word2)
    matchedLetter = totalLetter - len(setlst)
    deletionOperation  = totalLetter - 2*matchedLetter
    print(abs(deletionOperation))

