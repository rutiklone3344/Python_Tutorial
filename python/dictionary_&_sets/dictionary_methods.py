myDict = {
    "fast": "In a quick manner",
    "rutik": "A Coder",
    "ruu": [1,1,2,2],
    "nested": {"pratik":"yash"},
    1 : 2
}
# DICTIONARY METHODS
print(list(myDict.keys())) #prints the keys of the dictionary
print(myDict.values()) #prints the values of the dictionary
print(myDict.items()) #prints the key,value for all content of the dictionary
print(myDict)
updateDict = {
    "lovish": "friend",
    "divya" : "friend"
}
myDict.update(updateDict)# update the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("rutik2")) # returns NONE as rutik2 is not present in the dictionary
print(myDict["rutik2"]) # throws an error as rutik2 is not present in the dictionary
