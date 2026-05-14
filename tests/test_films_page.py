from playwright.sync_api import Page, expect

"""
Does films page have a header h1 thart says FILMS
"""

def test_films_has_title(page: Page):
    page.goto("http://127.0.0.1:5001/films")
    h1 = page.locator("h1")
    expect(h1).to_have_text("FILMS")
"""
Does my expected films from my database list correclty 
"""
def test_list_of_books_are_as_expected(page: Page):
    page.goto("http://127.0.0.1:5001/films")
    books = page.locator("li")
    expected_books = [
        
    ]