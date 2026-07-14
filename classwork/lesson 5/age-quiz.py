#take in users age and store in variable called age
#put a limit on how old someone can be. no higher than 100
#if user over 40 output "You're over the hill."
#if user is over 65 output "Enjoy your retirment!"
#if user is under 13 output "You qualify for the kiddie discount."
#if the user is 21 output "Congrats on your 21st!"
#For any other age output "Age is but a number."

#asks users age
age = int(input("Please enter your age: "))

#filters the age and gives the appropriate response
if(age > 100):
    print("Sorry you are dead")
elif(age >= 65):
    print("Enjoy your retirement!")
elif(age >= 40):
    print("You're over the hill.")
elif(age < 13):
    print("You qualify for the kiddie discount.")
elif(age == 21):
    print("Congrats on your 21st!")
else:
    print("Age is but a number.")            