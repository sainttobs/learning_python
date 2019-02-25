# creating a class

class Book():
    def __init__(self, name, price, publisher):
        """Initialize name, price and publisher"""

        self.name = name
        self.price = price
        self.publisher = publisher

    def hardback(self):
        """Simulate a hardback book"""
        print(self.name.title() + " is a hard back book")

    def softback(self):
        """Simulate a softback book"""
        print(self.name.title() + " is a softback book")

    def ebook(self):
        """Simulate an ebook"""
        print(self.name.title() + " is an ebook")

    def ebook_reader(self):
        """Simulate an ebook reader"""
        print("library: " + self.name.title() + ", " + str(self.price) + ", " + self.publisher.title() + ".")


my_book = Book('Elon Musk', 19.99, 'Virgin Books')
your_book = Book('Freak the Mighty', 29.99, 'Atlanta Books')
print("I am currently reading " + my_book.name.title())
print("This book cost $" + str(my_book.price) + " and it was published by " + my_book.publisher.title())

my_book.softback()
your_book.hardback()  # creating another instance of the book class
my_book.ebook_reader()