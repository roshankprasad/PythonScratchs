# sorting with the help of .sort() and sorted function...

# medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
# countries = sorted(medals , key = lambda x : medals[x])
# #print(countries)
# top_three = []
#
# x =0
# while x <3 :
#     top_three.append(countries[x])
#     x = x+1
# print(top_three)

#
# groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
#
# most_needed = sorted(groceries, key = lambda x : groceries[x],reverse=True)
# print(most_needed)


#def last_four(x):

#
# ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
# lst = []
# for id in ids:
#     lst.append(id - 17570000)
# sorted_ids= lst.sort()

# #
# def last_four(x):
#     lst = []
#     for val in x:
#         lst.append(str(val)[-4:])
#     lst = sorted(lst)
#     return lst
# ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
# sorted_ids = last_four(ids)
# print(sorted_ids)

#
# ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
# lst = sorted(ids, key=lambda x : str(x)[-4:])
# sorted_ids = lst
# print(sorted_ids)
#
# def last_four(x):
#     val = str(x)[-4:]
#     return int(val)
#
# ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
# sorted_ids = sorted(ids , key =last_four)
# print(sorted_ids)
# for val in ids:
#     print(last_four(val))

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
print(ex_lst[0][1])
lambda_sort = sorted(ex_lst, key=lambda x : x[1])
print(lambda_sort)


