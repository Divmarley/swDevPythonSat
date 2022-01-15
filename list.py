# mylist = ["apple", "banana", "cherry",1,3, "banana", "cherry",1,3]
# mylist.append(123)
# mylist.insert(0, "kofi")
# # print(len(mylist))
# # mylist[1] =  "kiwi"
# # mylist[-1] =  "paw"
# # mylist[-1] =  "paw"
# print(mylist)

# Extend List
# To append elements from another list to the current list, use the extend() method.
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]

# thislist.extend(tropical)

# print(thislist)

# Remove Specified Index
# The pop() method removes the specified index.
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("cherry")
# thislist.pop()
# thislist.pop()
# thislist.pop()
# print(thislist)


# thislist = ['apple', "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ['apple',  "cherry","banana",]
# thislist.sort()
# print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

"""

Method	       Description
append()	             Adds an element at the end of the list
clear()	         Removes all the elements from the list
copy()	         Returns a copy of the list
count()	         Returns the number of elements with the specified value
extend()	         Add the elements of a list (or any iterable), to the end of the current list
index()	         Returns the index of the first element with the specified value
insert()	         Adds an element at the specified position
pop()	         Removes the element at the specified position
remove()	         Removes the item with the specified value
reverse()	         Reverses the order of the list
sort()	         Sorts the list




"""