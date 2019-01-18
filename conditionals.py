#  using conditionals if-else statements

print("To continue enter your name")
name = input("Enter your name: ")

if name.title() == "Toba":  # use != to check for not equal to
    print("Welcome Mr. " + name.title())
else:
    print("No user found")