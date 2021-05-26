class employee:
    compant ="github"
    salary = 4500
    salarybonus = 500
    #totalsalary = 5000

    @property
    def totalsalary(self):
        return self.salary + self.salarybonus

    @totalsalary.setter
    def totalsalary(self , val):
        self.salarybonus = val - self.salary

e = employee()
print(e.totalsalary)
e.totalsalary = 6000
print(e.salary)
print(e.salarybonus)
