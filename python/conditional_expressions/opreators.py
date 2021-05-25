# *RELATION OPERATORS
''' Relation operators are used to evaluate conditons inside the if statements.
 some examples of relational operators are'''

# == equals
# >= greator than equal to
# <= less than equal to


# *LOGICAL OPERATORS
''' In pyton logical operatora operate on
conditional statements exg:'''

# and - True if both operands are true else false
# or  - True if at least one operands is true else false
# not - Inverts true to false & false to true
 
age = int(input("Enter your age: "))
if(age>34 and age<50):
    print("you can work with us")

age = int(input("Enter your age: "))
if(age>30 or age<50):
    print("you can work with us")


# * IN and IS 
a = [45, 56, 6]
print(435 in a)

a = None
if (a is None):
    print('yes')
else:
    print('no')


# IMP NOTES
# There can be any number of elif statements
# last else is executed only if all the condition inside elif fail.