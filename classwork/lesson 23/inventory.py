
#========The beginning of the class==========
class Shoe:

    # intialize attributes
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    # returns cost of shoe
    def get_cost(self):
        return self.cost


    # return quantity of shoe
    def get_quantity(self):
        return self.quantity


    # prints out information about the shoe when printing out class
    def __str__(self):
        return(f"Country: {self.country}\n"
              f"Code: {self.code}\n"
              f"Product: {self.product}\n"
              f"Cost: {self.cost}\n"
              f"Quantity: {self.quantity}\n")


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data(items):
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this
    data and append this object into the shoes list. One line in this file
    represents data to create one object of shoes. You must use the
    try-except in this function for error handling. Remember to skip
    the first line using your code.
    '''

    # checks if file exists, puts each line in text file in a list
    try:
        with open("inventory.txt", "r+", encoding="utf-8") as file:
            text_file = file.readlines()
            text_file.pop(0)
    
    except FileNotFoundError as error:
        print("file does not exist.\n")
        print(error)

    # iterates through list of shoes and splits them into a shoe object
    for i in range(len(text_file)):

        split = text_file[i].split(",")
        items.append(Shoe(split[0], split[1], split[2],
                           split[3], int(split[4])))

    return items
    



def capture_shoes(items):
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    try:
        # asks user input for shoe object
        country = input("Please enter the Country: ")
        sku = input("Please enter the SKU: ")
        product = input("Please enter the product name: ")
        cost = int(input("Please enter the cost of the shoe: "))
        quantity = int(input("Please enter the inventory stock: "))
        print("")

        items.append(Shoe(country.capitalize(), sku.upper(),
                           product.title(), cost, quantity))
    
    except Exception as error:
        print("Invalid entry")
        print(error)
        print("")

        return items

    try:
        # saves the header of txt file into the temp_storage
        with open("inventory.txt", "r+", encoding="utf-8") as file:
            
            header = file.readline()
            temp_storage = [header]

        # fills rest of temp_storage with the shoe objects and converts
        # them into a string to store on text file.
        with open("inventory.txt", "w", encoding="utf-8") as file:
            for i in range(len(items)):

                temp_string = (f"{items[i].country},"
                f"{items[i].code},{items[i].product},"
                f"{items[i].cost},{items[i].quantity}\n")
                temp_storage.append(temp_string)

            file.writelines(temp_storage)
        
    except FileNotFoundError as error:
        print("missing file")
        print(error)
    
    return items




def view_all(items):
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

    # iterates through the list of shoes and prints the objects
    for i in items:
        print(i)




def re_stock(items):
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

    # initalize placeholder variables
    temp_index = 0
    temp_storage = items[0]

    # compares the quantity of all the shoes in the list and save the lowest
    for i in range(len(items) - 1):

        if int(temp_storage.quantity) > int(items[i + 1].quantity):
            temp_storage = items[i + 1]
            temp_index = i + 1


    try:
        # prints lowest quanity item and asks user if they would like to
        # add more
        print(f"Lowest quanity: \n{temp_storage}")
        update_qt = int(input("How much inventory would like to add: "))
        items[temp_index].quantity = int(
            items[temp_index].quantity) + update_qt
        print(f"product: {items[temp_index].product}\n"
              f"quantity: {items[temp_index].quantity}\n"
              f"quantity has been updated by: {update_qt}\n")


        try:
            # saves the header of txt file into the temp_storage
            with open("inventory.txt", "r+", encoding="utf-8") as file:
                
                header = file.readline()
                temp_storage = [header]

            # fills rest of temp_storage with the shoe objects and converts
            # them into a string to store on text file.
            with open("inventory.txt", "w", encoding="utf-8") as file:
                for i in range(len(items)):

                    temp_string = (f"{items[i].country},"
                    f"{items[i].code},{items[i].product},"
                    f"{items[i].cost},{items[i].quantity}\n")
                    temp_storage.append(temp_string)

                file.writelines(temp_storage)
            
        except FileNotFoundError as error:
            print("missing file")
            print(error)

    except Exception as error:
        print("Invalid entry. Please try again.")
        print(error)
        update_qt = 0




def search_shoe(items, target):
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

    # splits target and only comepares numbers
    num_target = target.lower().split("sku")

    # interates through the list of shoes and return targets if found
    for i in range(len(items)):

        # splits sku from the number code so it is not reauired to type sku
        # every time
        temp_storage = ""
        temp_storage = items[i].code.lower().split("sku")
        if temp_storage[-1].lower() == num_target[-1].lower():
            return items[i]
    
    return f"SKU not found\n"


def value_per_item(items):
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

    # iterates through the list. prints out the quantity * cost for
    #  total value
    for i in range(len(items)):

        print(f"Product: {items[i].product}, \n"
              f"Total value: $"
              f"{(int(items[i].cost) * int(items[i].quantity)):.2f}\n")
        
        
    



def highest_qty(items):
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

    # initalize placeholder variables
    temp_storage = items[0]

    # compares the quantity of all the shoes in the list and save the lowest
    for i in range(len(items) - 1):

        if int(temp_storage.quantity) < int(items[i + 1].quantity):
            temp_storage = items[i + 1]
        

    print(f"Now On Sale!: \n{temp_storage}")
    



#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

read_shoes_data(shoe_list)

choice = 0
while input != 6:

    print("1. View All Inventory.\n"
          "2. Add New Shoe to Inventory\n"
          "3. Restock Shoes\n"
          "4. Look up Shoe by SKU\n"
          "5. Total Value of all Shoes\n"
          "6. Set Shoe Sale\n"
          "7. exit\n")
    
    try:
        choice = int(input("Please select and option 1-7: "))
        print("")

        # runs view_all function
        if choice == 1:
            view_all(shoe_list)
            
        elif choice == 2:
            capture_shoes(shoe_list)

        # runs re_stock function
        elif choice == 3:
            re_stock(shoe_list)
            print("")
            
        # runs search shoe function
        elif choice == 4:
            sku = input("Enter Shoe SKU: ")
            print(search_shoe(shoe_list, sku))
        
        # runs value_per_item function
        elif choice == 5:
            value_per_item(shoe_list)
            
        # runs highes_qty function
        elif choice == 6:
            highest_qty(shoe_list)
            
        # exits the program
        elif choice == 7:
            break
        
        # catch if user enters an invalid number option
        else:
            print("\nInvalid selection. Please try again.\n")

    except Exception as error:
        print(f"\nInvalid selection. Please try again.\n"
              f"{error}\n")