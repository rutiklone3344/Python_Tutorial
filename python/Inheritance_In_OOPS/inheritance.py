# INHERITANCE
''' 
Inheritance is a way of creating new class from an existing class

We can use the methods and attribute of employee in programmer object
Also we can overwrite or add new attribute and methods in programmers class

'''
class Employee:                    # --> parent class
    company = "google"

    def showDetails(self):
        print("This is an Employee")

class programmer(Employee):        # --> child class OR derived class
    Language = "Python"
    company  = "Youtube"

    def getLanguage(self):
        print(f"The language is{self.Language}")
    
    def showDetails(self):
        print("This is an Programmer!")

o = Employee()            # --> o is object
o.showDetails()
print(o.company)

p = programmer()
p.showDetails()
print(p.company)