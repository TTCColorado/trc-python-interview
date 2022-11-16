"""
Tests for phase one
"""

import unittest
from grocery_app.grocery_list import GroceryList

class TestGroceryListPhase1(unittest.TestCase):
    """
    Test cases for first phase
    """

    def test_get_items(self):
        """
        Ensure get_items functions appropriately.
        """

        groceries = GroceryList()

        groceries.add_item("a", 10.0)
        groceries.add_item("b", 20.0)
        groceries.add_item("c", 33.12)

        grocery_map = groceries.get_items()

        self.assertEqual(grocery_map.get("a"), 10.0)
        self.assertEqual(grocery_map.get("b"), 20.0)
        self.assertEqual(grocery_map.get("c"), 33.12)

    def test_lookup_item(self):
        """
        Ensure lookup_item functions appropriately.
        """

        groceries = GroceryList()

        groceries.add_item("a", 12.0)
        groceries.add_item("b", 13.0)
        groceries.add_item("c", 14.33)

        self.assertEqual(groceries.lookup_item("a"), 12.0)
        self.assertEqual(groceries.lookup_item("b"), 13.0)
        self.assertEqual(groceries.lookup_item("c"), 14.33)

    def test_items_by_price(self):
        """
        Ensure items_by_price functions appropriately.
        """

        groceries = GroceryList()

        groceries.add_item("a", 40.0)
        groceries.add_item("b", 13.0)
        groceries.add_item("c", 14.33)

        items = groceries.items_by_price()

        self.assertListEqual(items, ['a', 'c', 'b'])



if __name__ == "__main__":
    unittest.main()
