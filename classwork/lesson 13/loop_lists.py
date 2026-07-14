#define a list of strings of your 5 favorite movies
#loop over the list. For each item in the list print out
#   "Movie: " plus the movie's name.

movies = ["Gurren Laggan", "The Godfather", "Lawrence of Arabia", 
          "There will be blood", "Spotlight"]

for i, j in enumerate(movies):
    print(f"Movie {i}: {j}")
    