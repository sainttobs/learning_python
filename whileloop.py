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