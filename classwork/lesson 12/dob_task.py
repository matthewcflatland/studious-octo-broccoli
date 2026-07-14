#read file and separtes names and ages in 2 lists
#

#lists for the 2 categories
names = ["Names"]
ages = ["Birthdate"]

#opens file with all info
with open("DOB.txt", "r", encoding="utf-8") as file:

    #goes through each line in the text file
    for line in file:

        #splits each word into a list and adds the names to 1 string
        #and birthdate to a 2nd string
        temp = line.split()
        name = " ".join(temp[0:2])
        age = " ".join(temp[2:])

        #adds name to name list and bday to bday list
        names.append(name)
        ages.append(age)


#combines the lists into 1 string
name = "\n".join(names)
age = "\n".join(ages)


print(name)
print("\n" +age)    

