#program allows usuers to register for an exam venue
#ask how many students are registering
#loop the program based on number of students
#each iteration should ask for the student id number
#save id numbers to text file called reg_form.txt
#include dotted line after each student id



total_students = int(input("How many students are registering: "))

#create/open file to add to the end of the file.
file = open("reg_form.txt", "a+")

#loops through asking id and putting a dotted line per id.
for i in range(total_students):
    file.write(input("Please enter the student ID: "))
    file.write("\n\n-----------------------------------\n")

#closes file after taking ids
file.close()
    

    
    
