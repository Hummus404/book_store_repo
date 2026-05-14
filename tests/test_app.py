import sys
import os
# a hack line which allows us to import app without changing anything else. 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

"""
This test is going to create a test client and send a request then check to see if the response header status code is 200 which means it was successfull. 
"""
#descriptive test name 
def test_get_books_returns_a_200():
    #here is where we make the test client 
    client = app.test_client()
    # here is where we make the request
    response = client.get("/books")
    # hwre is where we assert that the respoins status code is 200 which is ok successfull
    assert response.status_code == 200

"""
This is a test which sets up a test client and sand sends a request then check to see if the response body is what we are expecting.
"""

def test_get_books_returns_all_the_books():
    client = app.test_client()
    response = client.get("/books_raw")
    assert response.json == [
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

"""
Test to see if a GET request for a list of authors is returned with a 200 ok status code and correct body
"""

def test_get_authors_returns_list_of_authors():
    client = app.test_client()
    response = client.get("/authors")
    assert response.json == [
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
    assert response.status_code == 200
