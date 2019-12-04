from typing import List, Any

string = "Hello"
print(string.swapcase())

studentsname: List[Any] = []
studentsscore: List[str] = []
for _ in range(int(input("enter size: "))):
    name = input("enter a name: ")
    score = input("enter number: ")
    studentsname.append(name)
    studentsscore.append(score)

print(studentsname)
print(studentsscore)