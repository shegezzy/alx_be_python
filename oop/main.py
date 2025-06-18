from book_class import Book as BookWithMagicMethods
from library_system import Book as LibraryBook, EBook, PrintBook, Library
from polymorphism_demo import Rectangle, Circle
from class_static_methods_demo import Calculator
import math

def main():
    # ====== Part 1: Book class with magic methods ======
    print("=== Magic Methods Demo ===")

    my_book = BookWithMagicMethods("1984", "George Orwell", 1949)
    print(my_book)
    print(repr(my_book))
    del my_book

    print("\n=== Library System Demo ===")

    # ====== Part 2: Library system with inheritance and composition ======
    my_library = Library()

    classic_book = LibraryBook("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()

    print("\n=== Polymorphism Demo ===")

    # ====== Part 3: Polymorphism and Method Overriding ======
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

    print("\n=== Class and Static Methods Demo ===")

    # ====== Part 4: Class vs Static Methods ======
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
