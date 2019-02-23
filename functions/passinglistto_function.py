# passing a list to a function

available_books = ['Freak The Mighty', 'Elon Musk', 'Purple Hibiscus', 'Half of a Yellow Sun']


def books_available(*books):
    for book in books:
        print('The book ' + book + " is available")


def book_description(author_name, book_type="non-fiction"):
    print("\nThis is a " + book_type + " book")
    print("The author of the book is " + author_name.title())
