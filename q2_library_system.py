catalog = {}
borrowed_books = []
members = set()
def add_book():
    book_id = int(input("Enter Book ID : "))
    title = input("Enter Book Title : ")
    author = input("Enter Author Name : ")
    year = int(input("Enter Year : "))
    catalog[book_id] = (title, author, year)
    print("Book Added Successfully")
def register_member():
    member_id = int(input("Enter Member ID : "))
    members.add(member_id)
    print("Member Registered")
def borrow_book():
    book_id = int(input("Enter Book ID to borrow : "))
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print("Book Borrowed")
    else:
        print("Book Not Available")
def return_book():
    book_id = int(input("Enter Book ID to return : "))
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print("Book Returned")
    else:
        print("Book was not borrowed")
def show_available_books():
    print("\nAvailable Books")
    for book_id in catalog:
        if book_id not in borrowed_books:
            book = catalog[book_id]
            print(book_id, "-", book[0], "-", book[1], "-", book[2])
while True:
    print("\n===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show Available Books")
    print("6. Exit")
    choice = int(input("Enter choice : "))
    if choice == 1:
        add_book()
    elif choice == 2:
        register_member()
    elif choice == 3:
        borrow_book()
    elif choice == 4:
        return_book()
    elif choice == 5:
        show_available_books()
    elif choice == 6:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")
