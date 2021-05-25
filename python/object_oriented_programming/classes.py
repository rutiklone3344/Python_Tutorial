# A class is the blue print from which specific objects are created
'''class (
    1. class.variable = A variable that is shared by all instances of a class.
    2. instance.variable = Instance variable unique to each isinstance
    3. Data.Member = A class variable or instance variable tht holds data associated with a class and its objects
)'''

class rc_company:
    employeeID =192
    salary = 500

rutik = rc_company()
pratik = rc_company()

print(f"EmployeeId:",rutik.employeeID, f"Employee Salary",rutik.salary)
print(f"EmployeeId:",pratik.employeeID, f"Employee Salary",pratik.salary)




'''
# Class Attributes
An attribute that belongs to the class rather than a particular object

Example:
       class Employee:
           company = "google"    -> [specify to each class]

        Rutik = Employee()       -> [object instantiation]
        Rutik.company
        Employee.company = "YouTube" ->[changing class attribute]
'''



'''
# Instance Attribute
An attribute that belongs to the instance(object) Assuming the class from previous example:

Rutik.name = "Rutik"
Rutik.salary = "10k"

NOTE Instance attribute take preference over class attribute during assignment & reterival

'''