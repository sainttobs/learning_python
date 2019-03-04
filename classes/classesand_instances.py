# Creating a new ereader class


class Ereader():
    """A class to represent an ereader."""

    def __init__(self, make, model, backlight, battery, screen_type):
        """Initialize the attribute to describe an ereader"""
        self.make = make
        self.model = model
        self.backlight = backlight
        self.battery = battery
        self.screen_type = screen_type
        self.library_count = 0

    def get_ereader_name(self):
        """Return a formatted descriptive name for our ereader"""
        long_name = self.make + ' - ' + self.model + ' - ' + self.backlight + ' - ' + self.battery + ' - ' + self.screen_type
        return long_name.title()

    def read_library_count(self):
        """Show the amount of books in our Library"""
        print("You have " + str(self.library_count) + " book in your kindle library.")

    def update_library_count(self, ebook_count):
        """Set the library count"""
        self.library_count = ebook_count

    def increment_library_count(self, purchased_ebooks):
        """Add our new ebooks to our library count"""
        self.library_count += purchased_ebooks


# my_new_ereader = Ereader('Amozon Kindle', 'Paperwhite', 'Adjustable Backliht',
# 'Several Months of Backlight','300 dpi')

# print(my_new_ereader.get_ereader_name())

# my_new_ereader.update_library_count(87)
# my_new_ereader.increment_library_count(9)
# my_new_ereader.read_library_count()

# INHERITANCE
class KindleFire(Ereader):
    """Represent aspects of am ereader specific to a Kindle Ereader
    Then initialize attributes specific to a kindle fire"""

    def __init__(self, make, model, backlight, battery, screen_type):
        """Initialize attributes for the kindle Fire"""

        super().__init__(make, model, backlight, battery, screen_type)


my_kindle_fire = KindleFire('amazon', 'kindle fire', 'backlight', '12 hour battery light', 'color screen')
print(my_kindle_fire.get_ereader_name())