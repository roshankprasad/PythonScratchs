# filedata = open("project_twitter_data.csv",'r')
# contents = filedata.readlines()
# header_row = contents[0].strip()
# print(header_row)
#
# for sentence in contents[1:10]:
#     row_string  = sentence.strip().split(',')
#     print('{} , {} , {}'.format(row_string[0],row_string[1],row_string[2]))


# filedata = open("postive_words.txt",'r')
# contents = filedata.readlines()
# header_row = contents[0].strip()
# print(header_row)
# for sentence in contents[1:]:
#     row_string  = sentence.strip()
#     # print('{} , {} , {}'.format(row_string[0],row_string[1],row_string[2]))
#     print(row_string)

#
# punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# # list of positive words to use
# positive_words = []
# with open("positive_words.txt") as pos_f:
#     for lin in pos_f:
#         if lin[0] != ';' and lin[0] != '\n':
#             positive_words.append(lin.strip())
# negative_words = []
# with open("negative_words.txt") as neg_f:
#     for lin in neg_f:
#         if lin[0] != ';' and lin[0] != '\n':
#             negative_words.append(lin.strip())
#
# print(positive_words)
# print(negative_words)
# print(pos_f)
# print(neg_f)

#
# txt = "#Amazing"
# x = txt.replace(txt,txt.strip('#'))
# print(x)
#----------------------------------------------

# punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# print(punctuation_chars)
# txt = input()
# lst = []
# for punct in punctuation_chars:
#     print(punct)
#     txt = txt.replace(punct,'')
# # word = txt.replace(".",'')
# # string = txt.replace(,)
# # print(txt)
# # print(word)


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
print(positive_words)
print(len(positive_words))
#
# sentence = input()
# def get_pos(sentence):
#     pass
#
#
# pos_word = ['happy','happy2','happ4']
# sentence = "i am roshan kumar happy wonderful good best awesome  "

def get_pos(string):
    sentencelst = []
    sentencelst = string.strip().split()
    #print(sentencelst)
    count = 0
    for word in sentencelst:
        if word in positive_words:
            count +=1
    return count
print(get_pos(input()))