class employee:
    company = "camel"
    salary = 200
    location = "mumbai"

    #def changeSalary(self , sal):
    #     self.__class__.salary = sal

    @classmethod
    def changesalary(cls, sal):
        cls.salary = sal

e = employee()
print(e.salary)
e.changesalary(300)
print(e.salary)
print(employee.salary)

'''
A class method is a method which is bound to the class and not the object of the class.
@classmethod decorator is used to create a class method
'''