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


my_new_ereader = Ereader('Amozon Kindle', 'Paperwhite', 'Adjustable Backliht', 'Several Months of Backlight','300 dpi')

print(my_new_ereader.get_ereader_name())
my_new_ereader.read_library_count()