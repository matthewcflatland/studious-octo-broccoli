#ask user to enter a sentence
#display the length of the string 
#Find the last letter in sentence. Replace every occurrence of the letter with @
#print the last 3 characters backwards
#create a five letter word that is made up of the first 3 characters and the last two characters

#word = "this is a test sentence"
str_manip = input("Please enter a sentence: ")

#displays length of the string
length = len(str_manip)
print(length)

#replaces last letter of word with @
last_letter = str_manip[length-1]
new_word = str_manip.replace(last_letter, "@")
print(new_word)

#print last 3 characters backwards
last_word = str_manip[-3:]
print(last_word[::-1])

#create 5 letter word first 3 chars and last 2 chars
five_word = str_manip[0:3] + str_manip[-2:]
print(five_word)