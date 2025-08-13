# book_class.py

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        try:
            print(f"Deleting {self.title}")
        except Exception:
            # During interpreter shutdown, attributes may already be cleared
            pass

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
