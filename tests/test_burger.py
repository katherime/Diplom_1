import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE as sauce, INGREDIENT_TYPE_FILLING as filling
from data import DefaultBurgerData


class TestBurger:

    @pytest.mark.parametrize('name, price', [('black bun', 100),
                                             ('white bun', 200),
                                             ('red bun', 300)
                                             ])
    def test_burger_set_buns_all_variations(self, name, price):
        burger = Burger()
        bun = Bun(name, price)
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.parametrize('ingredient_type, name, price', [(sauce, 'hot sauce', 100),
                                                              (sauce, 'sour cream', 200),
                                                              (sauce, 'chili sauce', 300),
                                                              (filling, 'cutlet', 100),
                                                              (filling, 'dinosaur', 200),
                                                              (filling, 'sausage', 300),
                                                              ])
    def test_burger_add_all_variations_of_ingredient(self, ingredient_type, name, price):
        burger = Burger()
        ingredient = Ingredient(ingredient_type, name, price)
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    @pytest.mark.parametrize('ingredient_type, name, price', [(sauce, 'hot sauce', 100),
                                                              (sauce, 'sour cream', 200),
                                                              (sauce, 'chili sauce', 300),
                                                              (filling, 'cutlet', 100),
                                                              (filling, 'dinosaur', 200),
                                                              (filling, 'sausage', 300),
                                                              ])
    def test_burger_remove_all_variations_of_ingredient(self, ingredient_type, name, price):
        burger = Burger()
        ingredient = Ingredient(ingredient_type, name, price)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert ingredient not in burger.ingredients

    def test_burger_move_ingredient(self, mock_bun, mock_sauce_ingridient, mock_filling_ingridient):
        burger = DefaultBurgerData.create_defailt_burger(mock_bun, mock_sauce_ingridient, mock_filling_ingridient)
        burger.move_ingredient(0, 1)
        assert mock_sauce_ingridient == burger.ingredients[1]

    def test_burger_get_price(self, mock_bun, mock_sauce_ingridient, mock_filling_ingridient):
        burger = DefaultBurgerData.create_defailt_burger(mock_bun, mock_sauce_ingridient, mock_filling_ingridient)
        assert burger.get_price() == DefaultBurgerData.burger_price

    def test_burger_get_receipt(self, mock_bun, mock_sauce_ingridient, mock_filling_ingridient):
        burger = DefaultBurgerData.create_defailt_burger(mock_bun, mock_sauce_ingridient, mock_filling_ingridient)
        assert burger.get_receipt() == DefaultBurgerData.receipt_text
