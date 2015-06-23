__author__ = 'snalam200'
from GroceryStore.src.infrastructure.building import Building
from decimal import Decimal


class GroceryStore(Building):
    def __init__(self):
        self.aisles = {
            'Bread': 10,
            'Milk': 10,
            'Chicken_Nuggets': 10,
            'Pizza': 10,
            'Eggs': 10,
            'Vegetables': 10,
            'Fruits': 10
        }

        self.prices = {
            'Bread': Decimal(2),
            'Milk': Decimal(3),
            'Chicken_Nuggets': Decimal(4.20),
            'Pizza': Decimal(5.23),
            'Eggs': Decimal(1.23),
            'Vegetables': Decimal(3.23),
            'Fruits': Decimal(4.23)
        }

        self.stock_room = {
            'Bread': 20,
            'Milk': 20,
            'Chicken_Nuggets': 20,
            'Pizza': 20,
            'Eggs': 20,
            'Vegetables': 20,
            'Fruits': 20
        }