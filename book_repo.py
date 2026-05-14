from book import Book

class BookRepo:

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM books")
        books = []
        for row in rows:
            item = Book(row["title"], row["author"],row["id"])
            books.append(item) 
        return books
    
    def create(self, book):
        self.connection.execute("INSERT INTO books (title, author) VALUES (%s, %s)", [book.title, book.author])
        return None
    

    # DO NOT USE THE BELOW YOU WILL GET SQL INJECTED AND DIE 
    # def create(self, book):
    #     self.connection.execute(f"INSERT INTO books (title, author) VALUES ('{book.title}', '{book.author}')")
    #     return None