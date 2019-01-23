# creating a dictionary. A dictionary is a collection of key vale pairs just like Objects
book = {'author': 'Adeyefa Oluwatoba', 'price': 100}  # creating a dictionary

print(book['author'])

if 'title' in book:  # checking if a key exists in a dictionary
    print("The key title exists in the dictionary 'book.'")
else:
    print("The key title does not exist in the dictionary 'book'.")

book['title'] = "Freak The Mighty"  # adding a new key to a dictionary

# using the .get() method to retrieve a value from a dictionary. the second parameter in the method is a default in case
# the key does not exists in the dictionary
# del book['price']  # to delete a key from a dictionary
print(book.get('title', 'the key "title" does not exist in the dictionary'))
print(book.get('genre', 'the key "genre" does not exist in the dictionary'))
print(book)

# looping through a dictionary with key-value pairs

for key, value in book.items():
    print("\nKey is: " + key)
    print("Value is: " + str(value))

# looping through a dictionary with keys and values
for detail in book.keys():  # with keys
    print(detail.title())

for value in book.values():  # with values
    print(value)

for value in set(book.values()):  # looping with set. Every value in a set must be unique i.e no repetition of values
    print(value)

# using dictionaries in a list

books = []  # creating an empty books list
for textbook in range(0, 10):  # looping through 10 times
    textbook = {'title': 'Engineering Mathematics', 'Price': '1500'}  # creating a textbook dictionary
    books.append(textbook)  # appending the textbook dictionary to the books list
print(books)

for textbook in books[0:5]:
    textbook['title'] = 'Software Engineering'  # editing the titles of the first the first 5 textbooks in the list
print(books[0:5])

# using a list in a dictionary

car = {
    'name': 'Tesla',
    'type': 'Electric Car',
    'extras': ['alloys wheels', 'climate control', 'rechargeable battery']
}

print(car)