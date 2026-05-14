from film import Film

class FilmRepo:

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM films")
        films = []
        for row in rows:
            item = Film(row["title"], row["genre"], row["release_year"], row["id"])
            films.append(item) 
        return films
    
    def create(self, film):
        self.connection.execute("INSERT INTO films (title, genre, release_year) VALUES (%s, %s, %s)", [film.title, film.genre, film.release_year])
        return None
    