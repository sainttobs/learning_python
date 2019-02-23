# passing a list to a function

available_books = ['Freak The Mighty', 'Elon Musk', 'Purple Hibiscus', 'Half of a Yellow Sun']


def books_available(*books):
    for book in books:
        print('The book ' + book + " is available")
