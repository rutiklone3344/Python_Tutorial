# Create a class with a class attribute a; 
# Create an object from it and set a directly using object a=0
# Does this change the class attribute?

class sample:
    a = "Rutik"

obj = sample()
obj.a = "vicky"
# sample.a = "vicky"  This will change the class attribute

print(sample.a)
print(obj.a)