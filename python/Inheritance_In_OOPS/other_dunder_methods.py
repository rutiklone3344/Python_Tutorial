class number:
    def __init__(self , num):
        self.num = num

    def __add__(self , num2):
        print("lets add")
        return self.num + num2.num

    def __mul__(self , num2):
        print("lets Multiply")
        return self.num * num2.num

    def __str__(self) -> str:
        return (F"Decimal number: {self.num}")

    def __len__(self):
        return 1

n= number(9)
print(n)
print(len(n))