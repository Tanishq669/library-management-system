class Book:
    def __init__(self, title, author, genre, year, available=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {'Available' if self.available else 'Checked Out'}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"


class Library:
    def __init__(self):
        self.books = [
            Book("1984", "George Orwell", "Dystopian", 1949),
            Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960),
            Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic", 1925)
        ]
        self.members = []

    def display_books(self):
        print("\nLibrary Collection:")
        for book in self.books:
            print(book)

    def linear_search_books(self, search_term):
        results = [book for book in self.books if (
            search_term.lower() in book.title.lower() or
            search_term.lower() in book.author.lower() or
            search_term.lower() in book.genre.lower()
        )]
        return results

    def sort_books(self, key):
        self.books.sort(key=lambda book: getattr(book, key).lower())

    def add_member(self, member):
        self.members.append(member)
        print(f"Added member: {member}")

    def display_members(self):
        print("\nLibrary Members:")
        for member in self.members:
            print(member)

    def add_book(self, title, author, genre, year):
        book = Book(title, author, genre, year)
        self.books.append(book)
        print(f"Added book: {book}")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Display Books")
        print("2. Search Books")
        print("3. Sort Books")
        print("4. Add Member")
        print("5. Display Members")
        print("6. Add Book")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            library.display_books()
        elif choice == '2':
            search_term = input("Enter title, author, or genre to search: ")
            results = library.linear_search_books(search_term)
            if results:
                print("\nSearch Results:")
                for book in results:
                    print(book)
            else:
                print("No books found.")
        elif choice == '3':
            sort_key = input("Sort by (title/author/year): ")
            if sort_key in ['title', 'author', 'year']:
                library.sort_books(sort_key)
                print(f"Books sorted by {sort_key}.")
            else:
                print("Invalid sort key.")
        elif choice == '4':
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            member = Member(name, member_id)
            library.add_member(member)
        elif choice == '5':
            library.display_members()
        elif choice == '6':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            year = input("Enter book year: ")
            library.add_book(title, author, genre, year)
        elif choice == '7':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
