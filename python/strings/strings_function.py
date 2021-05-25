story = '''once upon a time there was a youtuber named harry who
uploaded python course with notes'''

# string finctions
print(len(story))
print(story.endswith("notes")) #this function tellus whether the variable string ends with string or not
print(story.count("a")) #count the total number of occurnce of any character
print(story.capitalize()) #this function capitalize the first character of a given string
print(story.find("harry")) #find word & return in index (first occurance)
print(story.replace("harry", "codewithharry")) #this function replace the oldword with new word in the entire string
