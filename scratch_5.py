string = input("enter string")
position = int(input("enter position: "))
character = input("enter character: ")
#print(string[0:position] + string[position:])
list1 = list(string[0:position])
list2 = list(string[position+1:])
list1.insert(position,character)
list1 = list1 + list2
for ch in list1:
    print(ch,end="")

