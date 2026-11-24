# Personal Library Manager

# Each book contains:
# [title, author, genre, year, is_read]

library = []


# Display the main menu
def show_menu():
    print("\n========== PERSONAL LIBRARY ==========")
    print("1. Add a book")
    print("2. Show all books")
    print("3. Search for a book")
    print("4. Change reading status")
    print("5. Delete a book")
    print("6. Show library statistics")
    print("7. Filter books by genre")
    print("8. Sort books by title")
    print("9. Exit")


# Add a new book to the library
def add_book(books):

    title = input("Enter book title: ").strip()

    if title == "":
        print("Title cannot be empty.")
        return

    author = input("Enter author name: ").strip()

    if author == "":
        print("Author name cannot be empty.")
        return

    # Check whether the book already exists
    for book in books:
        if book[0].lower() == title.lower():
            print("This book already exists.")
            return

    genre = input("Enter book genre: ").strip().capitalize()

    if genre == "":
        print("Genre cannot be empty.")
        return

    year = input("Enter publication year: ").strip()

    if year.isdigit() is False:
        print("Invalid publication year.")
        return

    year = int(year)

    if year <= 0:
        print("Invalid publication year.")
        return

    # Ask for the reading status
    status = input("Have you read this book? (yes/no): ").strip().lower()

    if status == "yes":
        is_read = True

    elif status == "no":
        is_read = False

    else:
        print("Invalid reading status.")
        return

    # Create and store the new book
    new_book = [title, author, genre, year, is_read]

    books.append(new_book)

    print("Book added successfully.")


# Display all books
def show_books(books):

    if len(books) == 0:
        print("Your library is empty.")
        return

    print("\n========== BOOK LIST ==========")

    for book in books:

        print("------------------------------")
        print("Title:", book[0])
        print("Author:", book[1])
        print("Genre:", book[2])
        print("Year:", book[3])

        if book[4] is True:
            print("Status: Read")
        else:
            print("Status: Not Read")


# Search for a book by title or author
def search_book(books):

    search = input("Enter title or author: ").strip().lower()

    if search == "":
        print("Search input cannot be empty.")
        return

    found = False

    for book in books:

        if search in book[0].lower() or search in book[1].lower():

            print("\nBook Found:")
            print("Title:", book[0])
            print("Author:", book[1])
            print("Genre:", book[2])
            print("Year:", book[3])

            found = True

    if found is False:
        print("No matching book was found.")


# Change the reading status of a book
def change_status(books):

    title = input("Enter book title: ").strip().lower()

    for book in books:

        if book[0].lower() == title:

            print("1. Mark as read")
            print("2. Mark as not read")

            choice = input("Choose an option: ").strip()

            match choice:

                case "1":
                    book[4] = True
                    print("Book marked as read.")

                case "2":
                    book[4] = False
                    print("Book marked as not read.")

                case _:
                    print("Invalid option.")

            return

    print("Book not found.")


# Delete a book from the library
def delete_book(books):

    title = input("Enter book title to delete: ").strip().lower()

    for index in range(len(books)):

        if books[index][0].lower() == title:

            confirmation = input("Are you sure? (yes/no): ").strip().lower()

            if confirmation == "yes":
                books.pop(index)
                print("Book deleted successfully.")

            else:
                print("Deletion cancelled.")

            return

    print("Book not found.")


# Display library statistics
def show_statistics(books):

    total_books = len(books)
    read_books = 0
    unread_books = 0

    for book in books:

        if book[4] is True:
            read_books += 1

        else:
            unread_books += 1

    print("\n========== LIBRARY STATISTICS ==========")
    print("Total Books:", total_books)
    print("Read Books:", read_books)
    print("Unread Books:", unread_books)

    if total_books > 0:

        read_percentage = (read_books / total_books) * 100

        print("Reading Progress:", read_percentage, "%")

    else:
        print("No books available.")


# Generate books belonging to a specific genre
def get_books_by_genre(books, genre):

    for book in books:

        if book[2].lower() == genre.lower():
            yield book


# Filter books by genre
def filter_by_genre(books):

    genre = input("Enter genre: ").strip()

    if genre == "":
        print("Genre cannot be empty.")
        return

    found = False

    print("\n========== FILTERED BOOKS ==========")

    for book in get_books_by_genre(books, genre):

        print(book[0], "-", book[1], "-", book[3])

        found = True

    if found is False:
        print("No books found in this genre.")


# Sort books alphabetically
def sort_books(books, reverse_order=False):

    books.sort(
        key=lambda book: book[0].lower(),
        reverse=reverse_order
    )

    print("Books sorted successfully.")

    show_books(books)


# Main program
while True:

    show_menu()

    choice = input("\nChoose an option: ").strip()

    match choice:

        case "1":
            add_book(library)

        case "2":
            show_books(library)

        case "3":
            search_book(library)

        case "4":
            change_status(library)

        case "5":
            delete_book(library)

        case "6":
            show_statistics(library)

        case "7":
            filter_by_genre(library)

        case "8":

            print("1. A to Z")
            print("2. Z to A")

            sort_choice = input("Choose sorting order: ").strip()

            if sort_choice == "1":
                sort_books(library)

            elif sort_choice == "2":
                sort_books(library, True)

            else:
                print("Invalid sorting option.")

        case "9":
            print("Thank you for using Personal Library Manager.")
            break

        case _:
            print("Invalid menu option.")