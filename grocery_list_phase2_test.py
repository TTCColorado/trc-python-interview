"""
Tests for phase two
"""

import unittest
from grocery_app.grocery_list import GroceryList

class TestGroceryListPhase2(unittest.TestCase):
    """
    Test cases for second phase
    """

    def test_add_duplicate_fails(self):
        """
        Ensure adding a duplicate item fails with ValueError.
        """
        groceries = GroceryList()

        groceries.add_item("a", 10.0)

        with self.assertRaises(ValueError):
            groceries.add_item("a", 20.0)

if __name__ == "__main__":
    unittest.main()
