class Book:
    def __init__(self, title, author, year, genre, available):
        if not isinstance(year, int) or year < 0:
            raise ValueError("Year must be a positive integer.")
        if not isinstance(available, bool):
            raise ValueError("Availability must be a boolean (True or False).")
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {'Available' if self.available else 'Borrowed'}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        print("Book not found")
        return None

    def toggle_availability(self, title):
        book = self.search_book(title)
        if book:
            book.available = not book.available
            print(f"Availability of '{book.title}' toggled to {book.available}.")
        else:
            print("Book not found.")

    def available_books(self):
        print("Available books:")
        for book in self.books:
            if book.available:
                print(f" - {book}")

    def borrowed_books(self):
        print("Borrowed books:")
        for book in self.books:
            if not book.available:
                print(f" - {book}")

    def total_books(self):
        print(f"Total books in library: {len(self.books)}")


# Example usage
books = [
    Book("1984", "George Orwell", 1945, "Sci-Fi", False),
    Book("Animal Farm", "George Orwell", 1945, "Sci-Fi", False),
    Book("Brave New World", "Aldous Huxley", 1932, "Sci-Fi", True),
    Book("Fahrenheit 451", "Ray Bradbury", 1953, "Sci-Fi", False),
    Book("The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction", True),
]

library_parventa = Library()
for book in books:
    library_parventa.add_book(book)

library_parventa.search_book("1984")
library_parventa.toggle_availability("1984")
library_parventa.available_books()
library_parventa.borrowed_books()
library_parventa.total_books()