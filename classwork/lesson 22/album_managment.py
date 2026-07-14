#design a class called album
class Album:
    
    def __init__(self, album_name, album_artist, number_of_songs):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist
    
    def __str__(self):
        return(f"{self.album_name}, {self.album_artist}, {self.number_of_songs}")
    
    def songs(self):
        return self.number_of_songs


def list_print(items):
    for i in items:
        print(i)
    print("\n")    


#create a list with 5 albums and print it out
albums1 = [
    Album("Thriller", "Micheal Jackson", 7),
    Album("Hotel California", "Eagles", 3),
    Album("Back in Black", "AC/DC", 4),
    Album("The Bodyguard", "Whitney Houston", 6),
    Album("Falling into You", "Celine Dion", 5)
]

print("Here is album 1: ")
list_print(albums1)


#sort the list according to the number of songs
sorted_album1 = sorted(albums1, key=lambda song: song.number_of_songs)
print("Here is album 1 sorted by songs: ")
list_print(sorted_album1)


#swap the element at position 1 of albums1 with element at position 2
albums1[0], albums1[1] = albums1[1], albums1[0]
print("Here is album 1 with index 0 and 1 swapped")
list_print(albums1)


#create new list called album 2 and add 5 album objects to albums 2
albums2 = [
    Album("Led Zepplin IV", "Led Zepplin", 2),
    Album("Jagged Little Pill", "Alanis Morissette", 6),
    Album("21", "Adele", 5),
    Album("1", "The Beatles", 1),
    Album("Metalica", "Metalica", 5)
]


#print out list in albums 2
print("\nHere is albums 2: ")
list_print(albums2)    


#copy all the albums from albums1 into albums2
for i in albums1:
    albums2.append(i)


#add the following 2 albums int albums2:
albums2.append(Album("The Dark Side of the Moon", "Pink Floyd", 9))
albums2.append(Album("Oops!... I Did it Again", "Britney Spears", 16))


#sort the albums in albums2 alphabetically according to album name and print
sorted_album2 = sorted(albums2, key=lambda name: name.album_name.lower())
print("Here is album2 sorted alphabetically: ")
list_print(sorted_album2)


#search for album Dark Side of the moon in albums 2 and print out the index
print("Here is album list 2: ")
list_print(albums2)
for index, i in enumerate(albums2):
    if i.album_name.lower() == "the dark side of the moon":
        print(f"The Dark side of the Moon is in index: {index}")

        










