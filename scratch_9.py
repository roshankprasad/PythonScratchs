#we will do this function by slicing again again whenwever we found the substring
string = "abcdcdc"
sub_string = "cdc"
index = string.find(sub_string)

if index >= 0 :
    count  = 1
    for i in range(len(string)):
    newstring = string[index:len(string)]
    newstring.find() >=0
    count +=1
    index+sub_string

z = string.count(sub_string)
print(z)