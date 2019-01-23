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