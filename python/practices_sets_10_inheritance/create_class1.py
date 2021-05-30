#create a class pets from a class animals and further create class dog from pets.
#add a method bark to class dog

class animal:
    animalType = "mammal"

class pets(animal):
    petcolor = "white"

class dog(pets):
    @staticmethod
    def bark():
        print("Bow Bow!")

d = dog()
d.bark()