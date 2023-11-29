
class Movie:
    def __init__(self, title: str, genre: str, release_year: int, director: str):
        if not (title and genre and director):
            raise ValueError("Title, genre, and director must not be empty. Please enter a value.")
        elif release_year < 0:
            raise ValueError("Release year must be a positive integer. Please enter a valid value.")

        self.title = title
        self.genre = genre
        self.release_year = release_year
        self.director = director



    def display_info(self):
        print("Title:", self.title)
        print("Genre:", self.genre)
        print("Release year:", self.release_year)
        print("Directed by:", self.director)

    def set_genre(self, new_genre:str):
        valid_genres = ["Drama", "thriller","history", "comedy", "fantasy", "romance", "science", "fiction", "adventure", "sports", "action", "western", "horror", "musical","mystery"]
        self.new_genre = new_genre
        if new_genre.capitalize() in valid_genres:
            self.genre = new_genre.capitalize()
            print("New genre set")
        else:
            print("Please enter a valid genre")




class Comedy_movie(Movie):
    def __init__(self, title, genre, release_year, director, funny_level:int):
        super().__init__(title, genre, release_year, director)
        self.funny_level = funny_level

    def display_info(self):
        print("Title:", self.title)
        print("Genre:", self.genre)
        print("Release year:", self.release_year)
        print("Directed by:", self.director)
        print("Funny level:", self.funny_level)

class Drama_movie(Movie):
    def __init__(self, title, genre, release_year, director, emotion_level:int):
        super().__init__(title, genre, release_year, director)
        self.emotion_level = emotion_level

    def display_info(self):
        print("Title:", self.title)
        print("Genre:", self.genre)
        print("Release year:", self.release_year)
        print("Directed by:", self.director)
        print("Emotion level:", self.emotion_level)








movies = [
    Movie("The Batman","sience fiction", 2022, "Matt Reeves"),
    Movie("Napoleon", "history", 2023, "Ridley Scott"),
    Movie("Oppenheimer","drama", 2023, "Christopher Nolan"),
    Comedy_movie("Dumb and dumber", "comedy", 1994, "Christopher Nolan", 8),
    Comedy_movie("Dirty granpa", "comedy", 2016, "Dan Mazer", 8),
    Drama_movie("Gladiator", "drama", 2000, "Ridley Scott", 8),
    Drama_movie("The Godfather","Drama",1972, "Francis Ford Coppola/Mario Puzo", 10),
    Drama_movie("The Shawshank Redemption", "Drama", 1994, "Frank Darabont", 7)

]

for movie in movies:
    movie.set_genre("history(example for function set_genre")
    movie.display_info()
print("True genre---------------------------------------------------------------------------------->\n"
      "          ---------------------------------------------------------------------------------->\n")
for movie in movies:
    movie.display_info()