#excuse Generator
#madeby Roshankprasad
print("---- Excuse - Generator ----")
# birth_month = input("Birth month first three letters")
# phoneNumber_lastdigit = int(input("now phone number last digit"))
# excuse = ""
# month_dict = {}
# month_dict['jan'] = "Sister "
# month_dict['feb'] = "Dog "
# month_dict['mar'] = "Boss "
# month_dict['apr'] = "Brother "
# month_dict['may'] = "Uncle "
# month_dict['jun'] = "Dad "
# month_dict['jul'] = "Best Friend "
# month_dict['aug'] = "Aunt "
# month_dict['sep'] = "Twin "
# month_dict['oct'] = "Cat "
# month_dict['nov'] = "Grandma "
# month_dict['dec'] = "Second Cousin "
#
# phoneNumber_dict = {}
# phoneNumber_dict[1] = "got sick"
# phoneNumber_dict[2] = "came over unexpectedly"
# phoneNumber_dict[3] = "gave birth"
# phoneNumber_dict[4] = "has food posioning"
# phoneNumber_dict[5] = "is in labor"
# phoneNumber_dict[6] = "is in grave danger"
# phoneNumber_dict[7] = "needs a ride"
# phoneNumber_dict[8] = "got hit by a bus"
# phoneNumber_dict[9] = "is missing"
# phoneNumber_dict[0] = "chocked in a peanut"
#
# excuse = "My " + month_dict[birth_month] + phoneNumber_dict[phoneNumber_lastdigit]
# print(excuse)
# lst = []
# for word in phoneNumber_dict:
#     lst.append(phoneNumber_dict[word])
# print(lst)

# ----------2nd code for excuse genrator ----------
birthMonth = int(input("enter 'month in numbers'"))
if not 0<birthMonth<13:
    print("you have entered incorrect , please enter correct month in  numbers")
    birthMonth = int(input('''enter "month in numbers"'''))
lastdigit = int(input("enter 'last digit of phone number'"))
if not 0<=lastdigit<10:
    print("you have entered incorrect , please enter phone number last digit only")
    lastdigit = int(input('''enter "last digit"'''))
excuse = ""
nouns = ['Sister ', 'Dog ', 'Boss ', 'Brother ', 'Uncle ', 'Dad ', 'Best Friend ', 'Aunt ', 'Twin ', 'Cat ', 'Grandma ', 'Second Cousin ']
adjectives = ['got sick', 'came over unexpectedly', 'gave birth', 'has food posioning', 'is in labor', 'is in grave danger', 'needs a ride', 'got hit by a bus', 'is missing', 'chocked in a peanut']

excuse = "My " + nouns[birthMonth-1] + adjectives[lastdigit-1]
print(excuse)