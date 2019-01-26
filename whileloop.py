# using while loop to print from 1 - 10
num = 1
while num <= 10:
    print(num)
    num += 1

# using a flagto stop a while loop

prompt = "\n press q to quit this program"
prompt += "\n Enter your name: "

active = True# set the flag to True

while active:
    message = input(prompt)

    if message == "q":  # if the input message is q, quit the program
        active = False
    else:
        print(message)

# exiting a while loop using a break statement. Also use continue statement to *well* continue

prompt = "\nEnter q to quit \n Enter a book you have read"
while True:
    book = input(prompt)
    if book == "q":
        break
    else:
        print(book)

# using while loops with lists and dictionaries
unconfirmed_users = ['john', 'bull', 'my', 'son']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()  # the .pop() method removes a value from a list, you can also specify the
    # index of the value to be removed
    print("verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("The following users have been cnfirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# use .remove("value") to remove all instances of a specific value from a list, also use a while loop to loop
# through the list

# Populating a dictionary with user inputs, a property rental program

rental_properties = {}

# Set a flag to indicate we taking applications
rental_open = True

while rental_open:
    # prompt users for users name and address.
    username = input("\nWhat is your name? ")
    rental_property = input("What is the address of the property that you have to rent? ")

    # store the responses in a dictionary
    rental_properties[username] = rental_property

    # ask if the user knows anyone else looking to rent a property
    repeat = input("\nDo you know anyone who might like to rent out their property? ")
    if repeat == 'no':
        rental_open = False

    # adding property is complete

print("\n--- Property to rent ---")
for username, rental_property in rental_properties.items():
    print(username + " has " + rental_property + " to rent.")
