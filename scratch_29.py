def isPrime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        print(i)
        if num %i ==0:
            return False
        return True
lst = []
for i in range(int(input("enter a number"))):
    if isPrime(i) == True:
        lst.append(i)
print(lst)

