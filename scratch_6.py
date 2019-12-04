list1 = []
size = int(input("size: "))
for i in range(size):
    list1.append(int(input()))
print(list1)
list1.sort()
print(list1)
print(list1[len(list1)-2])