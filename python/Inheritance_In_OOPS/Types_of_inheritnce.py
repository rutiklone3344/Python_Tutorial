# Type of inheritance

'''
--> Types of Inheritance
1. Single inheritance
2. multiple inheritance
3. multilevel inheritance

'''

# Single inheritance
''' 
Single inheritance occurs when child class inherits only a single parent class
                Base       parent class
                 |               |
              Derived       child class
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


# Multiple Inheritance
'''
Multiple inheritance occurs when the child class inherit from more tha one parent
            parent 1                   parent 2
               |__________________________|
                            |
                          Child
'''
class employee:               # parent 1
    company = "visa"
    eCode = 120

class Freelancer:             # parent 2
    company = "Fiver"
    level = 0

    def upgradelevel(self):
        self.level = self.level + 1

class programmer(employee, Freelancer):    # Child
    name = "Rutik"

p = programmer()
p.upgradelevel()
print(p.level)


# Multi Level Inheritance
# When a child class become a parent for another child class
'''
                   parent
                     |
                   child 1
                     |
                   child 2 
'''
