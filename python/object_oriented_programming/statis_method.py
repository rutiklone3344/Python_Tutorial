# @statictmethod
'''
Sometimes we need a function that doesnt use the self parameter
we can define static method by using (@statictmethod)
'''

class Employee:
    company = "google"

    def getSalary(self , signature):
        print(f"Salary for this Employee working in {self.company} is {self.Salary}\n {signature}")
    
    @staticmethod
    def greet():
        print('Good Morning, sir')

pratik = Employee()
pratik.Salary = 20000
pratik.getSalary("Thanks")  #Employee.getSalary(pratik)
pratik.greet()