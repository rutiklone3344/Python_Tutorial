#__init__() constructor
''' __init__() is a special method which is first run s soon as the object is created'''
#__init__() Method is also known as constructor

# It takes self argument and can also take further arguments

class Employee:
    company = "google"
    
    def __init__(self , name, salary, subunit): #constructor
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The Salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")


    def getSalary(self , signature):
        print(f"Salary for this Employee working in {self.company} is {self.Salary}\n {signature}")
    
    @staticmethod
    def greet():
        print('Good Morning, sir')

pratik = Employee("pratik",1000, "youtube")
pratik.getDetails()