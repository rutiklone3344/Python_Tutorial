# Write a class train which has method to book a ticket,
# get status(no of seats) and get fare information of train
# running under indian railways

class train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("***************")
        print(f"The name of the train is {self.name}")
        print(f"The Total number of seats {self.seats}")
        print("***************")

    def getfareinfo(self):
        print(f"The price of the Ticket is: Rs.{self.fare}")

    def bookticket(self):
        if(self.seats>0):
            print(f"Your ticket has been Booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in tatkal")

    def cancleTicket(self):
        pass


interCity = train("Intercity: 3344", 900, 15)
interCity.getStatus()
interCity.getfareinfo()
interCity.bookticket()
interCity.bookticket()
interCity.getStatus()

