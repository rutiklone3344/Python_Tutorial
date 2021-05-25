''' operators in python
1. arithmetic operators => +,-,*,/
2. assignment operators => =,+=,-=
3. comparison operators => ==,>,<,>=,!=
4. logical  operators   => and,or,not    '''

a=3
b=5
# arithmetic operators
print("The value of 3+5 is",3+5)
print("The value of 3-5 is",3-5)
print("The value of 3*5 is",3*5)
print("The value of 3/5 is",3/5)

# assignment operators
a = 34
a += 2  #34+2=36
a -= 2  #36-2=34
a *= 2  #34*2=68
a /= 2  #68/2=34.0
print(a)

# comparison operators
b = (14<7)
b = (14>7)
b = (14<=7)
b = (14>=7)
b = (14==7)
b = (14!=7)
print(b)

# logical operators
bool1 = True
bool2 = False
print("the value of bool1 and bool2 is", (bool1 and bool2))
print("the value of bool1 or bool2 is", (bool1 or bool2))
print("the value of not bool2 is", (not bool2))
