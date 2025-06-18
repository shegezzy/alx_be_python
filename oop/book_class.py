class Book:
    def __init__(self, title, author, year):
        """
        Constructor: Initializes the Book instance with title, author, and publication year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor: Called when the object is about to be destroyed.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Informal string representation: Used by print() and str().
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official string representation: Used by repr() and for debugging.
        Should return a string that can recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
