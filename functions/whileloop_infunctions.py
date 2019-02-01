#   using while loop with a function


def get_name(firstName, lastName):
    fullname = firstName + ' ' + lastName

    return fullname.title()


while True:
    print("\nWhat is your name")
    print("Press q at any time to quit this program")

    firstName = input("Enter your first name: ")

    if firstName == 'q':
        break

    lastName = input("Enter your last name: ")
    if lastName == 'q':
        break

    name = get_name(firstName, lastName)
    print("\nHello " + name)