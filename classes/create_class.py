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