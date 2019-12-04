#
# lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
#
# def element(string):
#     return 'Fruit: ' +string
# map_testing = map(element,lst_check )



#
# people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
#
# print(people[0][0])
# #first_names = [name[1] for name in people]
# #b_countries = filter(lambda cont :'B' in cont,countries)

# passed = [name[0] for name in students if name[1]>=70 ]


# tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
#
# compri = [name['name'] for name in tester['info']]
#
# print(compri)
#
# L1 = [3, 4, 5]
# L2 = [1, 2, 3]
# L3 = []
#
# for i in range(len(L1)):
#     L3.append(L1[i] + L2[i])
#
# print(L3)


# L1 = [3, 4, 5]
# L2 = [1, 2, 3]
# L4 = list(zip(L1, L2))
# print(L4)


# L1 = [3, 4, 5]
# L2 = [1, 2, 3]
# L4 = list(zip(L1, L2))
# print(L4)
# L3 = []
# for (x1,x2) in L4:
#     L3.append(x1+x2)
# print(L3)

# L1 = [3, 4, 5]
# L2 = [1, 2, 3]
# L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]
# print(L3)


# L1 = [3, 4, 5]
# L2 = [1, 2, 3]
# L3 = list(map(lambda x: x[0] + x[1], zip(L1, L2)))
# print(L3)

#
# L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
# L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]
#
# L3  = [ x1+ x2 for (x1,x2) in list(zip(L1,L2)) if x1>10 and x2<5]

#
# species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']
#
# population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
#
# pop_info = list(zip(species,population))
# endangered = [name for (name,pop) in pop_info if pop<2500 ]