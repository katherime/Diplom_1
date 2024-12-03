from unittest.mock import Mock

import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE as sauce, INGREDIENT_TYPE_FILLING as filling
from data import DefaultBurgerData

class TestDatabase:


    def test_available_buns(self):
        database = Database()
        list_buns = database.available_buns()
        assert list_buns == [database.buns[0], database.buns[1], database.buns[2]]


    def test_available_ingredients(self):
        database = Database()
        list_ingredients = database.available_ingredients()
        assert list_ingredients == [database.ingredients[0], database.ingredients[1], database.ingredients[2],
                             database.ingredients[3], database.ingredients[4], database.ingredients[5]]

