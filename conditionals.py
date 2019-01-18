#  using conditionals if-else statements

print("To continue enter your name")
name = input("Enter your name: ")
age = input("Enter your age: ")

if name.title() == "Toba" and age == 19:  # use != to check for not equal to, using *and* statement both
    # conditions must be true, using *or* statement only one condition needs to be true.
    print("Welcome Mr. " + name.title())
else:
    print("No user found")

# check if a value exists in a list

regNames = ['toba', 'adeyefa', 'oluwatoba']

username = input("Enter your name: ")
if username in regNames:  # checking if the user already exists in the list,  use *not in* to check if user is not
    # in the list
    print("username already taken")
else:
    regNames.append(username)  # adding the new user to the list
    print("new user added")
    print(regNames)

