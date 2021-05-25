# Add a static method in problem 2 to greet the user with hello

class calculator:
    def __init__(self , num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} Square is: {self.number **2}")

    def cube(self):
        print(f"The value of {self.number} Cube is: {self.number **3}")

    def squareRoot(self):
        print(f"The value of {self.number} SquareRoot is: {self.number **0.5}")
    @staticmethod
    def greet():
        print("****Hello Welcome to the best calculator of the world****")

A = calculator(int(input("Enter the number: ")))
A.greet()
A.square()
A.cube()
A.squareRoot()
