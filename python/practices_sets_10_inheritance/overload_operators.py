# write a class complex to represent complex numbers, along with overload operator + & *
# which adds and miltuply them

# (a+bi)(c+di) = (ac-bd) + (ad+bc)i 

class complex:
    def __init__(self, r, i) -> None:
        self.real = r
        self.imaginary = i
    
    def __add__(self , c) -> None:
        return complex(self.real + c.real, self.imaginary + c.imaginary)

    def __mul__(self , c) -> None:
        mulReal = self.real*c.real - self.imaginary*c.imaginary
        mulImg  = self.real*c.imaginary + self.imaginary*c.real
        return complex(mulReal, mulImg)
    
    def __str__(self) -> str:
        return (f"{self.real} + {self.imaginary}i")
c1 = complex(1,4)
c2 = complex(8,5)
print(c1 + c2)
print(c1 * c2)