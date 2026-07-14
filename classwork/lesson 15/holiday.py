#goal is to calculate the users total holiday cost which includes:
    #plane cost, hotel cost, and car rental cost.
#get the following inputs:
    #city_flight the city they will be flying to
    #num_nights: the number of nights they will be staying at the hotel
    #rental_days: The number of days for which they will be hiring a car
#create the following 4 functions:
    #hotel_cost(): This function will take num_nights as an argument and return
        #the total cost for the hotel stay
    #plane_cost(): This function will take city_flight as an argument and return
        #a cost for the flight


def hotel_cost(x):
    """returns how much a night at a hotel will cost"""
    cost = x * 80.00
    return cost


def plane_cost(x):
    """returns how much the flight will cost invalid choice will return 0"""
    flight = x.replace(" ","")
    if flight.lower() == "chicago":
        return 200.00
    elif flight.lower() == "newyork":
        return 300.00
    elif flight.lower() == "lasvegas":
        return 150.00
    elif flight.lower() == "losangeles":
        return 100.00
    else:
        print("\nInvalid flight option.\n")
        return 0
    

def car_rental(x):
    """returns how much the car rental will cost per day"""
    rental = x * 50.00
    return rental


def holiday_cost(flight, night, rental):
    """returns the total cost of the holiday trip"""
    return (hotel_cost(night) + car_rental(rental) + plane_cost(flight))


#takes user input for where to fly, how many nights to stay, and how many days to rent.
flight = 0
while flight == 0:
    city_flight = input("Options:\n" 
                        "Chicago $200.00\n" 
                        "New York $300.00\n" 
                        "Las Vegas $150.00\n" 
                        "Los Angeles $100.00\n\n" 
                        "Where you would like to fly to: ")
    flight = plane_cost(city_flight) #if invaild will continue loop until
                                     #valid choice is selected

num_nights = int(input("Please enter how many nights you would like to stay: "))
rental_days = int(input("Please enter how many days you would like to rent the car: "))

#prints the calculations
print(f"The cost to fly to {city_flight} is: ${flight:.2f}")
print(f"The cost for the hotel is: ${hotel_cost(num_nights):.2f}")
print(f"The cost for the car rental is: ${car_rental(rental_days):.2f}")
print(f"The total cost of the holiday is: ${holiday_cost(city_flight, num_nights, rental_days):.2f}")