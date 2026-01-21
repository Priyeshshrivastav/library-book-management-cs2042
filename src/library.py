class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError(f"Book with ID {book_id} already exists.")
        
        self.books[book_id] = {
            'title': title,
            'author': author,
            'status': 'available'
        }
