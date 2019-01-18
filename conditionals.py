#  using conditionals if-else statements

print("To continue enter your name")
name = input("Enter your name: ")
age = input("Enter your age: ")

if name.title() == "Toba" and age == 19:  # use != to check for not equal to
    print("Welcome Mr. " + name.title())
else:
    print("No user found")
