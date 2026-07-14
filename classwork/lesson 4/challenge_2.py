#ask user favorite restaurant and store in string_fav
#ask user favorite number and store in int_fav store as int
#print both of these on separate lines
#after code is working try to cast string_fav as integer and explain what happens.

#ask user for favorite resturant and number
string_fav = input("What is your favorite resturant? ")
int_fav = int(input("What is your favorite number? "))

#prints the favorites
print(string_fav)
print(int_fav)

#casting string_fav as a integer
print(int(string_fav))
#The program crashes. The string needs to be a numerical value to be casted as an integer. 

