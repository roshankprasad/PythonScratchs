
outerlist = []
for lst in range(int(input())):
    innerlist= []
    for _ in range(1):
        innerlist.append(input())
        innerlist.append(float(input()))
    outerlist.append(innerlist)
#print(outerlist)

names =[]
lst = []
for listval in outerlist:
    lst.append(listval[1])
    if listval[1] ==  lst[0]:
        names.append(listval[0])

names.sort()
for name in names:
    print(name)
