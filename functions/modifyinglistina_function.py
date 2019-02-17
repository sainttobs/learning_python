# modifying a list in a function


available_books = ['Freak The Mighty', 'Elon Musk', 'Purple Hibiscus', 'Half of a Yellow Sun']
use_available_books = available_books[:]  # making a copy of a list to use in the function so the original list
# remains untampered with

def books_available(use_available_books):
    use_available_books.append('Last days at Forcados')
    del use_available_books[2]
    for use_available_book in available_books:
        print('The book ' + use_available_book + " is available")


books_available(available_books)