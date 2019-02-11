# passing a list to a function

available_books = ['Elon Musk', 'Freak the Mighty', 'Purple Hibiscus', 'Half of a Yellow Sun']


def books_available(books):
    for book in books:
        print('The book ' + book + " is available")


books_available(available_books)