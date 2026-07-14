# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key]) # changed k to key. K was undefined.

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!",
                         "maggie": "(Pacifier Suck)"
                         } #d'oh breaks the string because the the '

people = ['lisa', 'bart', 'homer'] #converted the other arguments to a list
print_values_of(simpson_catch_phrases, people) #this fuction only takes 2 arguments. 

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

