# tutorial on strings
firstName = "Oluwatoba"  # this is a string
lastName = "Adeyefa"
week = "THURSDAY".lower()  # .lower() method
address = "   3, Favour Street   "
name = "adeyefa oluwatobi \tadegoke".replace('tobi', 'toba')  # .replace() method \t to add tab and \n to add new line
movie = "What movie is this? 'All men must die?'".find("men")  # .find() method
line = 'What\'s your name'  # escaping a single quote

print("Hi " + firstName)  # String Concatenation
print(lastName + " " + firstName)
print(name.title())  # .title() method
print(movie)
print(line)
print(week)
print(name)
print(address.strip())  # .strip() method

