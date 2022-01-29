"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.



"""


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# # print(type(thisdict))
# # print(thisdict["brand"])
# # print(thisdict["model"])
# print(len(thisdict))



thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
# thisdict["brand"] ="kai"
# thisdict.update({"age": 2000,})
# thisdict.pop("colors")
# thisdict.popitem()
# thisdict.popitem()
# del thisdict["colors"]
# del thisdict

print(thisdict.items())




"""
Python has a set of built-in methods that you can use on dictionaries.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary


"""