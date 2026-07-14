# Design a program that determins the award a person competing in a triathlon will recieve
# accept input times for swimming, cycling and running.
# calculate and ouput the total time comeplete the triathlon
#Based on total time it will ouput the correct award based on the table

#input for the race times
swimming = int(input("How many minutes did it take to comeplete the swimming section? "))
running = int(input("How many minutes did it take to comeplete the running section? "))
cycling = int(input("How many minutes did it take to comeplete the cycling section? "))

#calculates total time and outputs it
time = swimming + running + cycling
print(f"The total time to compete the triathlon is {time}")

#outputs award based on time
if(time >= 0) and (time <= 100):
    print("Award: Provincial colours")
elif(time > 100) and (time <= 105):
    print("Award: Provincial half colours")
elif(time > 105) and (time <= 110):
    print("Award: Provincial scroll")
else:
    print("No award")

