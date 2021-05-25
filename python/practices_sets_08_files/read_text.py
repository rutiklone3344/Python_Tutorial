''' Write a program to read the text from a given file
 demo.txt and find out whether it contains the word distracted '''

file = open("demo.tex","r")
data = file.read()
print(data)
file.close()