# create a class employee and add salary and increment properties to it
# write a method salary after increment method with a @property decorator with a seeter which changes the valueof increment based on the salary


# SalaryAfterincrement = Salary * increment
class Employee:
    salary = 1000
    icrement = 1.5
    @property
    def salaryAfterIncrement(self):
        return (self.salary * self.icrement)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self , sai):
        self.icrement = sai/self.salary

e = Employee()
print(e.salaryAfterIncrement)

print(e.icrement)
e.salaryAfterIncrement = 2000
print(e.icrement)

