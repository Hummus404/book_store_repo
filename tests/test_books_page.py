from playwright.sync_api import Page, expect

def test_books_has_title(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    h1 = page.locator("h1")
    expect(h1).to_have_text("BOOKS")

def test_list_of_books_are_as_expected(page: Page):
    
    page.goto("http://127.0.0.1:5001/books")
    books = page.locator("li")
    expected_books = [
        'Learning Python by Umut Can',
        'Databases in a Nutshell by Hunter Khalil',
        'HTML for Newbies by Mia Jade',
        'The Art of SQL & Postgresql by Hunter Khalil',
        'Turkish Food Recipes by Mia Jade'
        #'Title A by Author A'
        ]

    actual_books = books.all_inner_texts()
    parsed_books = []

    for book in actual_books:
        parsed_book = book.replace('\n'," ")
        parsed_books.append(parsed_book)

    assert parsed_books == expected_books
    