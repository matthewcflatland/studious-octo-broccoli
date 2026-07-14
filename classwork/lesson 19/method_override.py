#create Adult class with following attributes:
    #Attributes: name, age, eye_color, and hair_color
    #A method called can_drive() which prints out the name of the person
     #and that they are old enough to drive.

class Adult:
    def __init__(self, name, age, hair_color, eye_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color


    def can_drive(self):
        print(f"{self.name} is {self.age} years old. They are old enough to drive.")
        

#create a subclass of Adult class named Child that has the same attributes,
 #but overrides the can_drive() method to print the person's name and that
 #they are too young to drive

class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is {self.age} years old. They are too young to drive.")


#Take user input that asks for name, age, hair color, and eye color.

try:
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    hair_color = input("Please enter your hair color: ")
    eye_color = input("Please enter your eye color: ")

#create some logic that determines if the person is 18 or older and create an
 #instance of the Child class. Once the object that has been created, call the
 #can_drive() method to print out whether the person is old enough to drive or not

    if age >= 18:
        person = Adult(name, age, hair_color, eye_color)
    else:
        person = Child(name, age, hair_color, eye_color)

    person.can_drive()

except Exception:
    print("Incorrect entry.")




