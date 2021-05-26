class person:
    country = "India"

    def __init__(self):
        print("Initializing Person.....\n")

    def takebreath(self):
        print("I am breathing...")

class employee(person):
    company = "goggle"

    def getsalary(self):
        print(f"salary is {self.salary}")

    def __init__(self):
        super().__init__()
        print("Initializing employee.....\n")

    def takebreath(self):
        print("I am an Employee so i am luckily breathing...")

class programmer(employee):
    company = "microsoft"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer.....\n")

    def getsalary(self):
        print("no salary for programmer")

    def takebreath(self):
        super().takebreath
        print("I am a programmer so i am breathing ++...")

p = person()
p.takebreath()
# print(p.company)  #throws an error

e = employee()
e.takebreath()
print(e.company)

pr = programmer()
pr.takebreath()
print(pr.company)
print(pr.country)

''' 
Super method is used to access the methods of a super class in the derived class.
'''