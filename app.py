from flask import Flask, render_template ,request, redirect
from database_connection import DatabaseConnection
from book_repo import BookRepo
from book import Book
from film import Film
from film_repo import FilmRepo
from user import User
from user_repo import UserRepo


# instantiate a Flask app object
app = Flask(__name__)

########################################################################
########################################################################

############### MAIN ###############

# GET request for rendering the films.html page
@app.route("/films", methods=['GET'])
def get_all_films():
    connection = DatabaseConnection()
    connection.connect()
    film_repo =FilmRepo(connection)
    films = film_repo.all()
    return render_template("films.html", films=films)

# creating route to POST /films:
@app.route('/films', methods= ['POST'])
def create_film():
    film_details= request.form
    db = DatabaseConnection()
    db.connect()
    repo = FilmRepo(db)
    film = Film(title=film_details["title"], genre=film_details["genre"], release_year=film_details["release_year"])
    repo.create(film)
    return redirect("/films")

# GET request for rendering the books.html page
@app.route("/books", methods=['GET'])
def get_all_books():
    connection = DatabaseConnection()
    connection.connect()
    book_repo = BookRepo(connection)
    books = book_repo.all()
    return render_template("books.html", books=books)

# POST request for creating a new book and adding it into the books database
@app.route('/books', methods=['POST'])
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_repo = BookRepo(connection)
    #creating a variable book_details and assigning form submission to it
    book_details = request.form
    
    book = Book(title=book_details["title"], author=book_details["author"])
    print(book)
    
    book_repo.create(book)
    books = book_repo.all()

    return redirect("/books")

# GET request for rendering the /signup_form.html page
@app.route("/users/new", methods=['GET'])
def get_users():
    return render_template("/signup_form.html")

# POST request ro send form details and create a user in the user database
@app.route("/users", methods=['POST'])
def create_new_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repo = UserRepo(connection)
    user_details = request.form
    user = User(username=user_details["username"], password=user_details["password"])
    user_repo.create(user)
    return redirect("/books")

########################################################################
########################################################################


############### ROUTE TO LOOP THROUGH A LIST ON HTML PAGE ###############
@app.route("/team", methods=['GET'])
def get_team():
    team = ["Umut", "Mia", "Khalil", "Arthur"]
    return render_template("team.html", team=team)

#########################################################################


# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"

# duplicate route
@app.route('/hello2', methods=['GET'])
def hello_again():
    return "Hello, hello and hello again!"

@app.route('/books_raw', methods=['GET'])
def get_books():
    
    books = [
    {
        "title": "The Gruffalo",
        "author": "Julia Donaldson"
    },
    {
        "title": "Ada Twist, Scientist",
        "author": "Andrea Beaty"
    },
    {
        "title": "The Girl Who Drank the Moon",
        "author": "Kelly Barnhill"
    },
    {
        "title": "Dragons in a Bag",
        "author": "Zetta Elliott"
    }
    ]
    return books

@app.route('/authors', methods=['GET'])
def get_authors():
    authors = [
    {
        "name": "Julia Donaldson",
        "dob": "1948-09-16"
    },
    {
        "name": "Andrea Beaty",
        "dob": "1961-10-08"
    },
    {
        "name": "Kelly Barnhill",
        "dob": "1973-01-01"
    },
    {
        "name": "Zetta Elliott",
        "dob": "1979-11-11"
    }
]
    return authors

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")





# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
