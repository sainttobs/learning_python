# modifying a list in a function


available_books = ['Freak The Mighty', 'Elon Musk', 'Purple Hibiscus', 'Half of a Yellow Sun']


def books_available(books):
    books.append('Last days at Forcados')
    del books[2]
    for book in books:
        print('The book ' + book + " is available")


books_available(available_books)