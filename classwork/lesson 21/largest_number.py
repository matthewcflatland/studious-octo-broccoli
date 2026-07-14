#define a function that takes a single argument

import random


def numbers(my_list):
    #variable to account for index of list
    length = len(my_list) - 1
    
    #if 0 returns largest number
    if length == 0:
        return my_list
    
    #will compare the last 2 numbers in list and delete the smaller number
    else:
        if my_list[length] < my_list[length - 1]:
            my_list.pop()

        else:
            my_list.pop(length - 1)


        #recursive fuction call
        return numbers(my_list)
    

#populates a random list of 10 integers
list_numbers = []
for i in range(10):
    list_numbers.append(random.randint(1, 100))    

#prints out the list and largets number
print(f"Random list of numbers: \n{list_numbers}")
print(f"Largest number in list: {numbers(list_numbers)}")