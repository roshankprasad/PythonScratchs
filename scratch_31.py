#anagrams
str1 = list(input())
str2 = list(input())

if len(str1) == len(str2):
    for char in str1:
        print(str2,char)
        str2.remove(char)
        print(str2)
    if str2 == []:
        print("anagrams")
    else:
        print('Not anagrams')
else:
    print("Not anagrams")