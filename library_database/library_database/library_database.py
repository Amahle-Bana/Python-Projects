import sqlite3

# CREATING 'ebookstore' SQlITE DATABASE
db = sqlite3.connect('ebookstore.db')

# EXECUTING DATABASE QUERY FOR 'Creating a table'
cursor = db.cursor()
cursor.execute('''
        CREATE TABLE Book (id INTEGER NOT NULL PRIMARY KEY,
                            title TEXT NOT NULL,
                            author TEXT NOT NULL,
                            qty INTEGER NOT NULL)
               ''')
db.commit()

# EXECUTING DATABASE QUERY FOR 'Inserting rows'
cursor = db.cursor()
# DECLARING THE CURRENT LIST AVAILABLE
registered_books = [(3001, 'A Tale Of Two Cities', 'Charles Dickens', 30),(3002, "Harry Potter and the Philosopher's Stone","J.K Rowling", 40),
                     (3003, "The Lion the Witch aand the Wardrobe", "C.S Lewis", 25), (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
                     (3005, "Alice in Wonderland", "Lewis Carroll", 12)]
# INSERTING THE CURRENT LIST AVAILABLE
cursor.executemany('''
                INSERT INTO Book (id, title, author, qty) VALUES(?,?,?,?)''', registered_books)
db.commit()

# INITIALIZING THE WHILE LOOP
while True:
    # BOOKSTORE OPTIONS INPUT
    question = int(input('''Choose An Option:
    1. Enter Book
    2. Update Book
    3. Delete Book
    4. Search Books
    0. Exit
    '''))
    # 'Enter Book' CONDITIONAL
    if question == 1:
        register_id = int(input("Enter An ID: "))
        register_title = input("Enter The Title Of The Book: ")
        register_author = input("Enter The Author's Name: ")
        register_qty = int(input("Enter The Quantity: "))

        register_book = (register_id, register_title, register_author, register_qty)
        cursor = db.cursor()
        cursor.execute('''
                INSERT INTO Book (id, title, author, qty) VALUES(?,?,?,?)''', register_book)
        db.commit()
    # 'Update Book' CONDITIONAL
    if question == 2:
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM Book''')
        for book in cursor:
            print(book)
        db.commit()
        question_id = int(input('''Select The ID Of The Book You Want To Update: '''))
        change_question = int(input('''
        Select The Data Type You Want To Update:
        1. id
        2. title
        3. author
        4. qty
        '''))
        if change_question == 1:
            id_change_question = int(input("Enter It's New ID: "))
            cursor = db.cursor()
            cursor.execute('''UPDATE Book SET id = ? WHERE id = ?''', (id_change_question, question_id))
            db.commit()

        if change_question == 2:
            title_change_question = (input("Enter It's New Title: "))
            cursor = db.cursor()
            cursor.execute('''UPDATE Book SET title = ? WHERE id = ?''', (title_change_question, question_id))
            db.commit()
        
        if change_question == 3:
            author_change_question = (input("Enter It's New Author: "))
            cursor = db.cursor()
            cursor.execute('''UPDATE Book SET author = ? WHERE id = ?''', (author_change_question, question_id))
            db.commit()
        
        if change_question == 4:
            qty_change_question = int(input("Enter It's New Quantity: "))
            cursor = db.cursor()
            cursor.execute('''UPDATE Book SET qty = ? WHERE  id = ?''', (qty_change_question, question_id))
            db.commit()
    # 'Delete Book' CONDITIONAL
    if question == 3:
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM Book''')
        for book in cursor:
            print(book)
        db.commit()
        question_delete = int(input("Select The ID Of The Book You Want To Delete:  "))
        cursor = db.cursor()
        cursor.execute('''DELETE FROM Book WHERE id=? ''', (question_delete,))
        db.commit()
    # 'Search Book' CONDITIONAL
    if question == 4:
        search_question_type = int(input('''Search For A Title or Author:
        1. Title
        2. Author
         '''))
        if search_question_type == 1:
            search_type = input("Search The Title: ")
            cursor = db.cursor()
            cursor.execute('''SELECT * FROM Book WHERE title=?''', (search_type,))
            print(list(cursor))
            db.commit()

        if search_question_type == 2:
            search_type = input("Search The Author: ")
            cursor = db.cursor()
            cursor.execute('''SELECT * FROM Book WHERE author=?''', (search_type,))
            print(list(cursor))
            db.commit()
    # 'Exit' CONDITIONAL
    if question == 5:
        exit()
        
