# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        # Note: exact deletion time may vary depending on Python's garbage collector
        try:
            print(f"Deleting {self.title}")
        except AttributeError:
            # In rare cases during interpreter shutdown attributes may already be gone
            pass

    def __str__(self) -> str:
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        return f"Book('{self.title}', '{self.author}', {self.year})"
