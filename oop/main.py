from book_class import Book as BookWithMagicMethods
from library_system import Book as LibraryBook, EBook, PrintBook, Library
from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    # ====== Part 1: Book class with magic methods ======
    print("=== Magic Methods Demo ===")

    # Create and demonstrate Book from book_class.py
    my_book = BookWithMagicMethods("1984", "George Orwell", 1949)
    print(my_book)
    print(repr(my_book))
    del my_book

    print()  # Separator

    # ====== Part 2: Library system using inheritance and composition ======
    print("=== Library System Demo ===")

    # Create a Library instance
    my_library = Library()

    # Use Book class from library_system.py here (not book_class.py)
    classic_book = LibraryBook("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

    print()  # Separator

    # ====== Part 3: Polymorphism and Method Overriding ======
    print("=== Polymorphism Demo ===")

    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
