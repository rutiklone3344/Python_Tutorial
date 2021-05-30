# Create a class c-2d vector and use it to create another class representing a 3-d vector.

class c2dvec:
    def __init__(self , i , j) -> None:
        self.icap = i
        self.jcap = j
    def __str__(self) -> str:
        return (f"{self.icap}i + {self.jcap}j")


class c3dvec(c2dvec):
    def __init__(self ,i,j, k) -> None:
        super().__init__(i,j)
        self.kcap = k

    def __str__(self) -> str:
        return (f"{self.icap}i + {self.jcap}j + {self.kcap}k")

v2d = c2dvec(1,3)
v3d = c3dvec(1,9,7)
print(v2d)
print(v3d)

