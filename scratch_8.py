#we will do this function by slicing again again whenwever we found the substring

string = "abcdcabcdc"
sub_string = "cdc"
index = string.index(sub_string)
if index >= 0 :
    cout=1
#if index < len(string):
while index != len(string)-1:
    # z = string.find(sub_string, index + 1, len(string) - 1)
    # print(z)
    if string.find(sub_string,index+1,len(string)-1) >= index :
        cout +=1
        index +=1
    else:
        index+=1
print(cout)