from csv import DictReader
import json

with open('books.csv', newline='') as books_file:
    books = DictReader(books_file)
    books_list = []
    for book in books:
        books_list.append(
            {'title': book['Title'], 'author': book['Author'], 'pages': book['Pages'], 'genre': book['Genre']})

with open('users.json', "r") as users_file:
    users = json.loads(users_file.read())
    users_list = []
    for user in users:
        users_list.append(
            {'name': user['name'], 'gender': user['gender'], 'address': user['address'],
             'age': user['age'], 'books': []})

result = users_list
user_item = 0
while len(books_list) > 0:
    book = books_list[0]
    result[user_item]['books'].append(book)
    books_list.remove(book)
    if user_item != len(users_list) - 1:
        user_item += 1
    else:
        user_item = 0

with open('result.json', 'w') as file:
    file.write(json.dumps(result, indent=3))