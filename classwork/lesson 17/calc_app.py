"""app should perform simple calculations and print and store the result in a text file
 2 functions 
   1: calcluate 2 numbers
   2: print previous equations and answers"""



def addition(num1, num2):
    '''adds 2 numbers'''
    return num1 + num2


def subtract(num1, num2):
    '''subtracts second number from first number'''
    return num1 - num2


def divide(num1, num2):
    '''divides first number by second number'''
    return num1/num2


def multipy(num1, num2):
    '''multiplies 2 numbers'''
    return num1 * num2


def equation(num1, num2, op, sum):
    '''prints and stores the equation on the text file'''
    equation = str(num1) + " " + op + " " + str(num2) + " = " + str(sum) + "\n"
    print(equation + "\n")
    with open("equations.txt", "a+", encoding="utf-8") as file:
        file.write(equation)

def operation(num1, num2, op):
    '''based on operation selected does calculations'''
    if op.lower() == "add":
        total = addition(num1, num2)
        operator = "+"
        return [operator, total]
            
    elif op.lower() == "sub":
        total = subtract(num1, num2)
        operator = "-"
        return [operator, total]
            
    elif op.lower() == "mul":
        total = multipy(num1, num2)
        operator = "*"
        return [operator, total]

    elif op.lower() == "div":
        if num2 == 0:
            print("Cannot divide by 0.")
            return False    

        total = divide(num1, num2)   
        operator = "/"
        return [operator, total]
            
    else:
        print("Invalid operator choice!")
        return False
                 


print("This program calculates does simple calculations" +
      " with 2 numbers or prints out stored calculations")

start = True
flag = True

while start == True:

    print("\ncalculate: user will enter 2 numbers and an operator " +
           "and the app will print the result.\n" +
          "log: will print out the previous calculations.\n" +
          "exit: will close the program.")


    choice = str(input("\nplease enter a selection: "))
    

    #takes 2 numbers from user and does calcuations
    if choice == "calculate":
        
        try:
            number_1 = int(input("Please enter the first number: "))
            number_2 = int(input("Please enter the second number: "))

            print("\nPlease select and operator: \n\n" +
                "add: adds both numbers together.\n" +
                "sub: subtracts second number from the first number.\n" +
                "mul: multiplies both numbers together.\n" +
                "div: divides the first number by the second number.\n")
            operator = str(input("Please enter your selection: "))

            
        except Exception:
            flag = False
        
        finally:
            if flag == False:
                 print("Invalid number selection. Please try again")
                 flag = True

            else:
                flag = operation(number_1, number_2, operator)
                if flag == False:
                    print("Please try again.")
                    flag = True
                else:
                    equation(number_1, number_2, flag[0], flag[1])
                    flag = True


    #prints from the equations.txt file
    elif choice.lower() == "log":
        try:  
            with open("equations.txt", "r+", encoding="utf-8") as file:
                equation_file = []
                equation_file = file.readlines()
                for i in equation_file:
                    print(i)

        except FileNotFoundError as error:
            print("\nThe file does not exist")
            print(error)

    #exits the program
    elif choice.lower() == "exit":
        start = False
    
    #for any incorrect input returns error msg.
    else:
        print("Invalid selection please try again!\n")