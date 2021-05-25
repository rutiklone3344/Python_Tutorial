# Write a python function to remove a given word from a string and strip it at the same time

def remove_word_strip(string , word):
    newstr = string.replace(word, "")
    return newstr.strip()

R = "this hey rutik"
remove = remove_word_strip(R, "this")
print(remove)