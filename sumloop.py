def sum():
	sum = 0
	active = True
	while active:
		n = int(input("Enter a number to add :"))
		sum += n

		if n == 0:
		 	active = False
	print("The sum of the numbers you entered is: " + str(sum))


sum()
		