#
# lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]
#
#
# #Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
# yellow = ""
# if "yellow" in lst[2]:
#     yellow = "yellow"
# print(yellow)
# # for var in lst[2]:
# #     if var == "yellow":
# #         yellow = var
# #Test to see if 4 is in the second list of lst. Save to variable ``four``
# for var in lst[1]:
#     if var == 4:
#         print(var)
#
# #Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
#
# for var in lst[0]:
#     if var == 'orange':
#         orange = var
#
# print(var)
#
# print(5 in lst[1])
#
# by = "You are"
# az = "doing a great "
# io = "job"
# qy = "keep it up!"
#
# message = by + " "+ az + io + " "+ qy
#
# print(message)

# sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
# print(len(sports))
# last = []
# for i in range(3):
#      print(i)
#      last.append(sports[-3+i])
#
# print(last)

# addition_str = "2+5+10+20"
# print(addition_str.split("+"))
#
# lst = addition_str.split("+")
# sum_val = 0
# for values in lst:
#     sum_val = sum_val + int(values)


# original_str = "The quick brown rhino jumped over the extremely lazy fox"
# original_lst = original_str.split(" ")
# print(original_lst)
# cnt = 0
# num_words_list = []
# for words in original_lst:
#     for _ in words:
#         cnt = cnt +1
#     num_words_list.append(cnt)
#     cnt = 0
# print(num_words_list)
#print(len(original_str))



# lett = ""
# for _ in range(7):
#     lett = lett + 'b'

# week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
# fahr_lst = week_temps_f.split(",")
# total_temp = 0
# for fahrenheit in fahr_lst :
#     total_temp = total_temp + float(fahrenheit)
# avg_temp = total_temp / len(fahr_lst)


#
# str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
#
# # Write your code here.
#
# for lst in str_list:
#     print(len(lst))


# several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
#
# for thing in several_things:
#     print(thing)
#
# for thingtype in several_things:
#     print(type(thingtype))

# rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
# rainfall_mi_lst = list(rainfall_mi.split(","))
# print(rainfall_mi_lst)
# num_rainy_months = 0
# for lst in rainfall_mi_lst:
#     if float(lst) > 3.0 :
#         num_rainy_months = num_rainy_months + 1
# print(num_rainy_months)

#
# sentence = "students flockf to the arb for a variety of outdoor activities such as jogging and picnicking"
# lst = sentence.split(" ")
# print(lst)
# cont = 0
# for word in lst :
#     wordlst = list(word)
#     if wordlst[0] ==  wordlst[-1]:
#         cont = cont + 1
# print(cont)

# items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
#
# acc_num = 0
# for accum in items :
#     if "w" in accum :
#         acc_num +=1
#

# sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
# items = list(sentence.split(" "))
# print(items)
# num_a_or_e = 0
# for accum in items:
#     if 'a' in accum or 'e' in accum:
#         num_a_or_e +=1
##    elif 'e' in accum:
##        num_a_or_e +=1


# s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
# #lst = list(s.split(" "))
# lst = list(s)
# vowels = ['a', 'e', 'i', 'o', 'u']
# #print(lst)
# print(lst)
# num_vowels = 0
#
# for accum in lst :
#     if accum in vowels :
#         num_vowels +=1
# print(num_vowels)

#
# sent = "The mall has excellent sales right now."
# wrds = sent.split()
# print(wrds)
# wrds[1] = 'store'
# new_sent = " ".join(wrds)
# print(new_sent)

#
# byzo = 'hello world!'
# c = 0
# for x in byzo:
#     z = x + "!"
#     print(z)
#     c = c + 1

# cawdra = ['candy', 'daisy', 'pear', 'peach', 'gem', 'crown']
# t = 0
# for elem in cawdra:
#     t = t + len(elem)
#     print(t)
# print(t)

#rest = ["sleep", 'dormir', 'dormire', "slaap", 'sen', 'yuxu', 'yanam']
# let = ''
# for phrase in rest:
#     let += phrase[0]
# print(let)

# str1 = "I love python"
# # HINT: what's the accumulator? That should go here.
# chars = []
# for ch in str1 :
#     chars = chars + list(ch)
# print(chars)

# scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
# scores_lst = list(scores.split())
# a_scores = 0
# for score in scores_lst:
#      if int(score) >= 90:
#          a_scores +=1
# print(a_scores)

# stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
# org = "The organization for health, safety, and education"
#
# stopwords = set(w.upper() for w in stopwords)
# acro = ''.join(i[0] for i in org.upper().split(' ') if i not in stopwords)
# print(stopwords)

# inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
#
# for items in inventory:
#     product = (items.split())[0]
#     number = (items.split())[1]
#     price = (items.split())[2]
#     print("The store has {} {} , each for {} USD.".format(number,product,price))
#
# print(inventory[0].split())
#


#
# nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}
#
# # Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
# data = False
# if 'data' in nested.keys():
#     data = True
#
# # Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
# twentyfour = False
# if 24 in nested['data']:
#     twentyfour = True
# print(twentyfour)
# print(nested['data'])
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
# whole = False
# if 'whole' not in nested['window']:
#     whole = True
# print(whole)
# # Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
# physics = False
# if 'physics' in nested.keys():
#     physics = True
# print(physics)


