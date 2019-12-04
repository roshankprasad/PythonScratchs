#list comprehension
things = [2,5,7,8,6,9]
mylist = [value * 2 for value in things]
print(mylist)

#map n filter function
def f(x):
    return x*x

mylst = map(f, things)
print(list(mylst))

#Api guide

import requests
import json

params = "rel_ant=day"
page = requests.get("http://api.datamuse.com/words", params)
txt = json.loads(page.text)
print(txt)
print(page.url)
print(page.text)


