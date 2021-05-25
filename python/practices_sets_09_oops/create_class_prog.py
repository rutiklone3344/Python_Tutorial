# create a class programmer for storing information of few programmers working at microsot

class programmer:
    company = "Microsoft"
    def __init__(self , name , product):
        self.name = name 
        self.product = product
    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")

rutik = programmer("Rutik","Skype")
pratik =programmer("Pratik","Github")
Nilesh =programmer("Nilesh",'instagram')

rutik.getInfo()
pratik.getInfo()
Nilesh.getInfo()