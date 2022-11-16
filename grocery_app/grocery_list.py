"""
Grocery shopping app
"""

class GroceryList:
    """
    A simple Grocery List
    """

    items: dict[str, float]

    def __init__(self):
        self.items = {}

    def add_item(self, item: str, cost: float) -> None:
        """
        Adds a grocery item of a given price.

        @param item: the name of the item being added.
        @param cost: the cost of the item being added.
        @raise ValueError: raises a ValueError when a duplicate item is added.
        """

        self.items[item] = cost

    def get_items(self) -> dict[str, float]:
        """
        Returns a dict of all the items added.

        @return: dict of grocery items
        """
        return self.items

    def lookup_item(self, item: str) -> float:
        """
        Looks up the price of a given item

        @param item: the name of the item to lookup
        @return: price of item
        """
        return self.items[item]

    def items_by_price(self) -> list[str]:
        """
        Gets items ordered by price in descending order.
        """
        return []
