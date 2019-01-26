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