#write a prog to alculate the grade of a student from his marks from the following scheme
''' 90-100 = A+
    80-90  = A
    70-80  = B
    60-70  = C
    50-60  = D
     <50   = F '''

marks = int(input("Enter yours makrs: "))

if marks>=90:
    grade = "A+"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D"

else:
    grade = "F"

print("Your grade is: " + grade)