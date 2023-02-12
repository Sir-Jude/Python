# Import "namedtuple" from "collections"
from collections import namedtuple

# Feed TWO paramethers ("name", "elements of the tuple") to "namedtuple" and assign it to a variable
tup = namedtuple("details", "name, surname, city")
# Feed the elements of the tuple to the variable and assign it to another variable
var = tup("Jude", "Smiley", "Berlin")                   
# Print the tuplenamed object...
print(var)                                              
# ...or trasform it into an actual tuple...
print(tuple(var))
# ...so it has the indexes
print(var[2])
# Use the method "._make" containing a LIST...
# containing as many elements as the original namedtuple
var = tup._make(["Jude", "Smiley", "Berlin" ])
print(var)
print()



# Import "deque" from "collections"
from collections import deque

# Create a list
people = ["Giulio", "Anne", "Jude"]
# Feed the list to deque and assign it to a variable
d = deque(people)
# Print the deque object...
print(d)
# Use the method .appendleft() to add an element in front of the list...
d.appendleft("Giuseppe")
print(d)
# ...or the method .popleft() to remove an element on the front of the list...
d.popleft()
print(d)
# ...or trasform it in a actual list...
print(list(d))
# ...BUT then you cannot use the method .appendleft() and .popleft()  
print()



# Import "Chainmap" from "collections"
# IMPORTANT: remember the capital "C" and "M"!!!
from collections import ChainMap

# Create two (or more) dictionaries
person1 = {"name": "Giulio", "surname": "Smiley"}
person2 = {"name": "Anne", "surname": "Hübner"}
# Feed te dictionaries to "ChainMap" and assign it to a variable
union = ChainMap(person1, person2)
print(union)
print()



# Import "Chainmap" from "collections"
# IMPORTANT: remember the capital "C"!!!
from collections import Counter

# Create a list
items = ["apple", "banana", "pear", "melon", "banana", "apple", "peach", "melon", "apple", "apple"]
# Feed the list to Counter and assign it to a variable
fridge = Counter(items)
# Print the Counter object...
print(fridge)
# ...or trasform it into a proper dictionary
print(dict(fridge))
# Use the method ".elements()" to get back the list, BUT with element ordered and grouped together
print(list(fridge.elements()))
# Use the method ".most_common()" to create a LIST of tuples...
# with most common element and how many times it is present
print(fridge.most_common())
# Create either another list...
eat = ["apple", "peach"]
# Use the method ".subtract()" to subtract the second list from the first
fridge.subtract(eat)
# Print the new dictionary
# IMPORTANT: the element "peach" is STILL there, but has now value ZERO! 
print(dict(fridge))
# ...or another dictionary
eat = {"apple":2, "melon":1}
# Use the method ".subtract()" to subtract the dictionary from the list
fridge.subtract(eat)
# Print the new dictionary
print(dict(fridge))



# Import "defaultdict" from "collections"
from collections import defaultdict

# Feed a datatype to "defaultdict" and assign it to a var
var_dic = defaultdict(list)
# Assign some pair key[value] to the dictionary
var_dic[1] = "Jude"
var_dic[2] = "Berlin"
# Try to print a not-existing key... 
print(var_dic[3])
# Python will return:
# 0  --> as a default int
# [] --> as a default dict
# ...
# Normally (without dafaultdict), Python will return an error.
