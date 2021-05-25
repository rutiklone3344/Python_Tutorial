# Self Parameter
'''
self replace to the instance of the class 
It is automatically passed with a function cell from an object

pratik.getsalary( )   -> [here self is pratik]
                 |    -> [equivalent to Employee getsalary(pratik)]
'''




class Employee:
    company = "google"
    def getSalary(self):
        print("Salary is 10k")

rutik = Employee()
rutik.getSalary() # Employee.getsalary(rutik)

def getSalary(self):
    print(f"Salary is {self.Salary}")

pratik = Employee()
pratik.Salary = 20,000
pratik.getSalary()