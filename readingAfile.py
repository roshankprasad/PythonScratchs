#Python code for - Reading in a file

# fileref = open("testfile.txt",'r')
# contents = fileref.read()
# print(len(contents))
# # lines = fileref.readlines()
# # print(len(lines))
# # # print(lines[:4])
# # # for lin in lines[:5]:
# # #     print(lin.strip())
# # # #print(contents)
# #
# # for lin in fileref:
# #     print(lin.strip())
# fileref.close()

#writing in a file


# file_obj = open("testfile.txt",'a')
# for number in range(11):
#     squarefn = number*number
#     print(squarefn,end =" ")
#     file_obj.write(str(squarefn))
#     file_obj.write(" ")
# file_obj.close();

#fileref = open("emotion_words.txt", 'r')
#contents = fileref.readlines()
# num_words = 0
# for sentence in contents.split():
#     #print(sentence)
#     num_words +=1
# num = len(contents)
# print(num)
# print(num_words)
# num = 0
# lines = fileref.readlines()
# for lin in lines:
#     num += 1
#     print(lin)
# print(num)
# print(contents)
# print(num_words)

#
# fileref = open("emotion_words.txt",'r')
# contents = fileref.read(30)
# print(contents)

# beginning_chars = ""
#
# for sentence in contents:
#     print(sentence)
#     beginning_chars = sentence
# print(beginning_chars)


# fileref = open("emotion_words.txt",'r')
# contents = fileref.readlines()
# print(contents)
# three = []
# for word in contents:
#     three.append(list(word.split())[2])
# print(three)
#
#

#
# fileref = open("travel_plans.txt",'r')
# contents = fileref.read(33)
# print(contents)
# first_chars = contents

# fileref = open("emotion_words.txt",'r')
# contents = fileref.readlines()
# print(contents)
# emotions = []
# for word in contents:
#     emotions.append(list(word.split())[0])
# print(emotions)
#
# fileref = open("school_prompt.txt",'r')
# contents = fileref.readlines()
# print(contents)
# three = []
# for word in contents:
#     three.append(list(word.split())[2])
# print(three)
#
# fileref = open("school_prompt.txt",'r')
# contents = fileref.read(30)
# beginning_chars = contents
#


#str1 = "sohanohan peter piper picked a peck of pickled peppers"
# freq = {}
# for character in str1:
#     if character in freq.keys():
#         freq[character] += 1
#     else:
#         freq[character] = 1
# print(freq)
# ks = freq.keys()
# print(ks)
# best_char = list(ks)[0]
# #print(best_char)
# for ch in ks:
#     if freq[ch] > freq[best_char] :
#         best_char = ch
#         print(ch)

# str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
# freq_words = {}
# for word in str1.split():
#     if word in freq_words.keys():
#         freq_words[word] +=1
#     else:
#         freq_words[word] = 1


# s1 = "hello"
# counts = {}
# for character in s1:
#     if character in counts.keys():
#         counts[character] += 1
#     else:
#         counts[character] = 1
#
#

# string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
# print(string1.lower())
# letter_counts = {}
# for word in string1.lower():
#     if word in letter_counts.keys():
#         letter_counts[word] += 1
#     else:
#         letter_counts[word] = 1
# print(letter_counts)
#


