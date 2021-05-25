#write a prog to find out whether a student is pass or fail if it requires total 40% and at least 35%
# in each subject to pass. assume 3 subjects and take marks as an inout from the user
sub1 = int(input("Enter marks subject 1: "))
sub2 = int(input("Enter marks subject 2: "))
sub3 = int(input("Enter marks subject 3: "))

if (sub1<35 or sub2<35 or sub3<35):
    print("You are fail because you have less than 35% in one of the subjects")
elif (sub1+sub2+sub3)/3 <40:
    print("you are fail due to total percentage less than 40")
else:
    print("congratulation! you are passed! ")        
