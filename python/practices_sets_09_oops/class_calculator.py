# Write a class calculator capable of finding square, cube and squareroot of a number

class calculator:
    def __init__(self , num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} Square is: {self.number **2}")

    def cube(self):
        print(f"The value of {self.number} Cube is: {self.number **3}")

    def squareRoot(self):
        print(f"The value of {self.number} SquareRoot is: {self.number **0.5}")

A = calculator(int(input("Enter the number: ")))
A.square()
A.cube()
A.squareRoot()
