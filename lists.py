months = ['january', 'february', 'april', 'may']  # creating a list

months.append('june')  # adding a new value to a list
print(months)
new_months = months[:]  # copying a list by slicing it.

print(new_months)

print(months[0:3])  # slicing a list
print(months[-2:])  # printing the last two elements in the list after slicing it

# looping through a slice
for month in months[-3:]:  # slicing the last three elements in the list
    print(month.title())

months.insert(2, 'march')  # inserting a new value to a list
print(months)

months.reverse()  # to reverse the order of the list

months.sort()  # sort list alphabetically user sort(reverse=True) to sort it reverse alphabetically

del months[5]  # deleting a value from a list
print(months)

months.pop(1)  # using the .pop() method.
print(months)

months.remove('april')  # using the .remove() method
print(months)
print(len(months))  # find the number of elements in a list

# Looping Through a List with for loop

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',
          'december']
for month in months:  # using for loop to loop through a list
    print(month.title() + "\n")
    print("The next month is :  ")

for value in range(1, 7):  # using the range function
    print(value)

numbers = list(range(1, 90, 2))  # creating a list of odd number less than 90. It adds 2 to each number
print(numbers)

# create a list of the squares of numbers 1 - 10
squares = []  # creating the list
for value in range(1, 11):  # for loop in range of 1 - 11
    square = value ** 2  # find the square of each element in the squares list
    squares.append(square)  # append the element to the list
print(squares)

digits = [2, 10, 5, 7]
print(min(digits))  # use max() to get maximum and sum() to get the sum



