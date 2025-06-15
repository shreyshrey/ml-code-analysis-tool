import unittest

class TestDuplicateRemoval(unittest.TestCase):
    def test_no_duplicates(self):
        self.assertFalse(check_for_duplicates([1, 2, 3]))

    def test_single_duplicate(self):
        self.assertTrue(check_for_duplicates([1, 2, 1]))

    def test_multiple_duplicates(self):
        self.assertTrue(check_for_duplicates([1, 1, 1]))

if __name__ == '__main__':
    unittest.main()