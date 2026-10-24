class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        if title in self.books:
            print("Book already exists!")
        else:
            self.books[title] = {
                "author": author,
                "available": True
            }
            print("Book added successfully!")

    def issue_book(self, title):
        if title not in self.books:
            print("Book not found!")
        elif self.books[title]["available"]:
            self.books[title]["available"] = False
            print("Book issued successfully!")
        else:
            print("Book is already issued!")

    def return_book(self, title):
        if title not in self.books:
            print("Book not found!")
        elif not self.books[title]["available"]:
            self.books[title]["available"] = True
            print("Book returned successfully!")
        else:
            print("This book was not issued!")

    def display_books(self):
        print("\nAvailable Books:")

        found = False

        for title, details in self.books.items():
            if details["available"]:
                print("Title:", title)
                print("Author:", details["author"])
                found = True

        if not found:
            print("No books are currently available.")


# Create a library object
library = Library()

# Menu-driven program
while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Available Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(title, author)

    elif choice == "2":
        title = input("Enter book title to issue: ")
        library.issue_book(title)

    elif choice == "3":
        title = input("Enter book title to return: ")
        library.return_book(title)

    elif choice == "4":
        library.display_books()

    elif choice == "5":
        print("Thank you for using the library!")
        break

    else:
        print("Invalid choice! Please try again.")