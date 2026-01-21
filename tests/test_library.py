import unittest
from src.library import Library

class TestLibrarySprint1(unittest.TestCase):
    def setUp(self):
        self.lib = Library()

    def test_add_book_success(self):
        self.lib.add_book(1, "The Great Gatsby", "F. Scott Fitzgerald")
        self.assertIn(1, self.lib.books)
        self.assertEqual(self.lib.books[1]['title'], "The Great Gatsby")
        self.assertEqual(self.lib.books[1]['author'], "F. Scott Fitzgerald")
        self.assertEqual(self.lib.books[1]['status'], "available")

    def test_add_book_duplicate_id(self):
        self.lib.add_book(1, "Book 1", "Author 1")
        with self.assertRaises(ValueError):
            self.lib.add_book(1, "Book 2", "Author 2")

class TestLibrarySprint2(unittest.TestCase):
    def setUp(self):
        self.lib = Library()
        self.lib.add_book(1, "The Hobbit", "J.R.R. Tolkien")

    def test_borrow_book_success(self):
        self.lib.borrow_book(1)
        self.assertEqual(self.lib.books[1]['status'], 'borrowed')

    def test_borrow_book_already_borrowed(self):
        self.lib.borrow_book(1)
        with self.assertRaises(ValueError):
            self.lib.borrow_book(1)

    def test_borrow_book_not_found(self):
        with self.assertRaises(ValueError):
            self.lib.borrow_book(999)

    def test_return_book_success(self):
        self.lib.borrow_book(1)
        self.lib.return_book(1)
        self.assertEqual(self.lib.books[1]['status'], 'available')

    def test_return_book_not_found(self):
        with self.assertRaises(ValueError):
            self.lib.return_book(999)

class TestLibrarySprint3(unittest.TestCase):
    def setUp(self):
        self.lib = Library()
        self.lib.add_book(1, "1984", "George Orwell")

    def test_report_header(self):
        report = self.lib.generate_report()
        self.assertIn("Book ID | Title | Author | Status", report)

    def test_report_content(self):
        report = self.lib.generate_report()
        self.assertIn("1 | 1984 | George Orwell | available", report)
        
    def test_report_borrowed_status(self):
        self.lib.borrow_book(1)
        report = self.lib.generate_report()
        self.assertIn("1 | 1984 | George Orwell | borrowed", report)

if __name__ == '__main__':
    unittest.main()
