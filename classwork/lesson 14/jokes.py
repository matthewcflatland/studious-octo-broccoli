#create a joke generator with random module
#create a list of jokes with their punchlines
#use random module to display a random joke each time the code runs


import random

#list of jokes
jokes = ["What do you call it when a snowman has a temper tantrum? \nA meltdown.",
         "Why are elevator jokes so good? \nBecause they work on so many levels.",
         "What do you call advice from a cow? \nBeef tips.",
         "Why are pediatricians always so patient? \nBecause they have little patients.",
         "Why did the scarecrow win an award? \nBecause he was outstanding in his field."]

#generates a random number between 1 and 5
randomizer = random.randint(1,5)

#selects which joke based on ranomzier
if randomizer == 1:
    print(jokes[0])
elif randomizer == 2:
    print(jokes[1])
elif randomizer == 3:
    print(jokes[2])
elif randomizer == 4:
    print(jokes[3])
else:
    print(jokes[4])

