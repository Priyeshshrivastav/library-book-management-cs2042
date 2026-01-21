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

if __name__ == '__main__':
    unittest.main()
