#take a user input as a string
#while string not john add string to a list until John is entered.
#print out the list of incorrect names

#initalizing list and user input
string_list = []
user_input = ""

#loops until john is entered
while user_input.lower() != "john":
    user_input = input("Please enter a string: ")

    #adds string to list if it is not john
    if user_input.lower() == "john":
        break
    else:
        string_list.append(user_input)

#prints the list
print(string_list)
