# creating an empty set
b = set()
print(type(b))

# sets methods #

# adding values to an empty set
b.add(4)
b.add(5)
b.add(5) # 5 will not add in set . bcoz set is non repetitive elements.
b.add((4,5,6)) # we can add tuples in sets. tuples are not changeable.

# accessing elements
b.add({4:5}) # we cannot add list or dictionary to sets
print(b)

# length of the set
print(len(b)) # prints the length of this sets

# removal of an item
b.remove(5) # removes from set b
b.remove(10) #throws an error while trying to remove 15 (which is not present ins set)
print(b)

b.pop() #
b.clear() # clear the set b
b.union({8,11}) #returns a new set with all items from both set
b.intersection({8,11}) # returns a set which contains only items in both set 