# write a program to create a dictionary of hindi words with values as their english translation provide user with an option to ;ook it up

d = {
    "namaste": "hello",
    "pankha":  "fan",
    "dabba":   "box",
    "vastu":   "item"
}
print("options are", d.keys())
a = input("Enter the hindi word: ")
print("The meaning of your word is:", d[a]) #this line show error if key is not present in dictionary
print("The meaning of your word is:", d.get(a)) #this line will not show error . bocz we'r using (get)