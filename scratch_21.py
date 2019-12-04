#Advanced and Optional Paramters for Function

# def greeting(name,greeting="Hello ", excl="!"):
#     return greeting + name + excl
#
# print(greeting("Bob"))
# print(greeting(""))
# print(greeting("Bob", excl="!!!"))

# Below is a function, sum, that does not work.
# Change the function definition so the code works.
# The function should still have a required parameter, intx, and an optional parameter,
# intz with a defualt value of 5.

# def sum(intx,intz=5, ):
#     return intz + intx

# def test(intx , opt_bool = True , dict1={2:3, 4:5, 6:8}):
#     if opt_bool == False:
#         return opt_bool
#     else :
#         if intx in dict1.keys():
#             return dict1[intx]
#
# def checkingIfIn(string, direction=True,
#                  d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
#     if direction == True:
#         if string in d.keys():
#             return True
#         else:
#             return False
#     else:
#         if string not in d.keys():
#             return True
#         else:
#             return False

# def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
#     if direction == True:
#         if a in d:
#             return d[a]
#         else:
#             return False
#     else:
#         if a not in d:
#             return True
#         else:
#             return d[a]
#
# res = checkingIfIn("apple")
# print(res)


