# lst = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
# setlst = set(lst)
# for element in setlst:
#     d[element] = 1
# print(d)

# migratory birds problem on hackerRank
# lst = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
# d = {}
# for element in lst:
#     if element in d.keys():
#         d[element] +=1
#     else:
#         d[element] = 1
# print(d)
# ks = d.keys()
# best_key = list(ks)[0]
# print(best_key)
# for element in d:
#     if d[best_key] < d[element]:
#         best_key = element
# print(best_key)


# sock merchant problem in hackerrrank
# # lst = [10, 20, 20, 10,10, 30, 50, 10,20]
# lst = [1,1,3,1,2,1,3,3,3,3]
# d = {}
# for element in lst:
#     if element in d.keys():
#         d[element] +=1
#     else:
#         d[element] = 1
# print(d)
# cont = 0
# for element in d.keys():
#     d[element]=int(d[element] / 2)
#     cont +=d[element]
# print(cont)

