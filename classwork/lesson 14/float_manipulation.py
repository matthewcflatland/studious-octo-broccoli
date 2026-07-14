#import statistics module and use its built in fuctions to complete this 
    #task
#ask the user to enter 10 floats and store in a list                    done
#find the total of all the numbers and print the result                 done    
#find the index of the maximum and print the result                     
#find the index of the minimum and print the result                     
#calculate the average of the numbers and round of 2 decimal places     
#find the median number and print the result                            

import statistics

#intialize variables/list
float_num = []
total = 0

#ask user for 10 float and store in the list
for i in range(10):
    float_num.append(float(input(f"Please enter a float {i + 1}: ")))

#sum of all inputted numbers
print(f"total sum of all inputted numbers: {sum(float_num)}")

#max and minium of all inputted numbers
print(f"maximum: {max(float_num)}")
print(f"minimum: {min(float_num)}")

#average of al inputted numbers
print(f"average: {statistics.mean(float_num)}")

#the median of all inputted numbers
print(f"median: {statistics.median(float_num)}")