# Connect to the SQLite database
import mysql.connector as s
conn=s.connect(host='localhost',user='root',passwd='root',database='book')
cursor=conn.cursor() 


# Create a table for books
cursor.execute('CREATE TABLE IF NOT EXISTS books (id int PRIMARY KEY,title char(40),author char(40),isbn char(40))')
conn.commit()

# Create a table for patrons
cursor.execute('CREATE TABLE IF NOT EXISTS patrons (id int PRIMARY KEY,name char(40),email char(20))')
conn.commit()

# Create a table for checkouts
cursor.execute('CREATE TABLE IF NOT EXISTS checkouts (id INT PRIMARY KEY,book_id int,patron_id int,due_date DATE FOREIGN KEY (book_id) REFERENCES books (id),FOREIGN KEY (patron_id) REFERENCES patrons (id))')
conn.commit()

# Function to add a book
def add_book(title, author, isbn):
    cursor.execute('INSERT INTO books (title, author, isbn) VALUES (%s,%s,%s)', (title, author, isbn))
    conn.commit()
    print("Book added successfully!")

# Function to add a patron
def add_patron(name, email):
    cursor.execute('INSERT INTO patrons (name, email) VALUES (%s,%s)', (name, email))
    conn.commit()
    print("Patron added successfully!")

# Function to check out a book
def checkout_book(book_id, patron_id, due_date):
    cursor.execute('INSERT INTO checkouts (book_id, patron_id, due_date) VALUES (%s,%s,%s)', (book_id, patron_id, due_date))
    conn.commit()
    print("Book checked out successfully!")

# Function to list all books
def list_books():
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    for book in books:
        print(f"{book[0]}. {book[1]} by {book[2]} (ISBN: {book[3]})")

# Function to list all patrons
def list_patrons():
    cursor.execute('SELECT * FROM patrons')
    patrons = cursor.fetchall()
    for patron in patrons:
        print(f"{patron[0]}. {patron[1]} (Email: {patron[2]})")

# Main menu
while True:
    print("\nLibrary Management System")
    print("1. Add a book")
    print("2. Add a patron")
    print("3. Check out a book")
    print("4. List all books")
    print("5. List all patrons")
    print("6. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        add_book(title, author, isbn)
    elif choice == "2":
        name = input("Enter patron name: ")
        email = input("Enter email: ")
        add_patron(name, email)
    elif choice == "3":
        list_books()
        book_id = int(input("Enter book ID to check out: "))
        list_patrons()
        patron_id = int(input("Enter patron ID: "))
        due_date = input("Enter due date (YYYY-MM-DD): ")
        checkout_book(book_id, patron_id, due_date)
    elif choice == "4":
        print("\nList of Books:")
        list_books()
    elif choice == "5":
        print("\nList of Patrons:")
        list_patrons()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

# Close the database connection
conn.close()
