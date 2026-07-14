#define a fuction that takes 2 arguments:
# a. A list of integers.
# b. A single integer that represents an index point.
import random

#recursion function adding numbers up to the index given
def sum_recursion(list, index):
    if index < 0:
        return 0
    else:
        return list[index] + sum_recursion(list, index - 1) 
    pass

#intalizing variables
numb_list = [2,4,6,8,10]
index = random.randint(0,4)

#print outs of list, random index, and sum
print(numb_list)
print(index)
print(sum_recursion(numb_list, index))
