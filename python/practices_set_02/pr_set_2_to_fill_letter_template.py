letter = ''' Dear <|NAME|>,
greetings from ABC coding comany. I am happy to tell you about your selection.
Your are selected!
Congraulations......
Have a great day ahead!
Date: <|DATE|>
'''
name = input("Enter your name: \n")
date = input("Enter date: \n")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)