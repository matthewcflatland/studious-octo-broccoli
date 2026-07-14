#to know the total worth of stock in the cafe
#create a list called menu with at least 4 items
#create a dictionary called stock that constains the stock value for
#   each item on your menu
#create another dictionary called price that should contain the prices
#   for each item on your menu.
#Calculate the total worth of the stock in the cafe and then store the
#   the results inside a variable called total_stock. you will need to
#   remember to loop through the appropriate dictionaries and lists to this
#print the results of the calculations


#intialize list menu
menu = ["coffee", "tea", "boba", "smoothe"]
total_stock = 0

#intialize dict stock
stock = {
    "coffee": 30,
    "tea": 50,
    "boba": 40,
    "smoothe": 24 }

#intialize dict price
price = {
    "coffee": 10,
    "tea": 5,
    "boba": 8,
    "smoothe": 9 }

#loops through menu list
for i in menu:
    
    #calculates total value of inventory and prints it out
    item_value = (stock[i] * price[i])
    total_stock += item_value
    print(f"Total value of {i} is {item_value}")

print(f"Total value is: {total_stock}")