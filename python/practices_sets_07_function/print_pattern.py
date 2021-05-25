# Write a function to print first n lines of the following pattern:
'''
* * *
* *             for n=3
*
'''

star = int(input("Enter your favourite number: "))
for i in range(star):
    print("*" * (star-i))    # print * n-i time
