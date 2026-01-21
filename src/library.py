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

    def borrow_book(self, book_id):
        if book_id not in self.books:
            raise ValueError(f"Book with ID {book_id} not found.")
        
        if self.books[book_id]['status'] != 'available':
            raise ValueError(f"Book with ID {book_id} is already borrowed.")
        
        self.books[book_id]['status'] = 'borrowed'

    def return_book(self, book_id):
        if book_id not in self.books:
            raise ValueError(f"Book with ID {book_id} not found.")
            
        if self.books[book_id]['status'] != 'borrowed':
             raise ValueError(f"Book with ID {book_id} is not borrowed.")

        self.books[book_id]['status'] = 'available'
