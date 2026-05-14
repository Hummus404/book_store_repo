# in a new file called `test_create_new_book.py`

from playwright.sync_api import Page, expect

"""
Test that filling in the form and submitting a new author and title adds the book to the database 
"""

def test_form_correctly_adds_book_to_database(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    page.get_by_placeholder("Title").fill("Title A")
    page.get_by_placeholder("Author").fill("Author A")
    page.get_by_role("button", name="Submit").click()
    books = page.locator('li')
    print(books.all_inner_texts())
    new_book = books.all_inner_texts()[-1]
    new_book = new_book.replace('\n'," ")
    
    assert new_book == "Title A by Author A"

    