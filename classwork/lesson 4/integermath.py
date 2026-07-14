#ask the user to input 3 integers
#print out the following:
#sum of all the numbers
#first number minus the 2nd number
#third number multiplied by the first number
#sum of all three numbers divided by the third number

#intake the 3 numbers
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))

#num1 = 5
#num2 = 6
#num3 = 7

#sum of all three numbers
sum = num1 + num2 + num3
print(sum)

#first number minus the second number
print(num1 - num2)

#Third number multiplied by the first number
print(num3 * num1)

#sum of all three numbers divided by the third number
print(int(sum/num3))