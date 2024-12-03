import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE as sauce, INGREDIENT_TYPE_FILLING as filling


class TestIngridients:

    @pytest.mark.parametrize('ingridient_type, name, price', [(sauce, 'hot sauce', 100),
                                                              (sauce, 'sour cream', 200),
                                                              (sauce, 'chili sauce', 300),
                                                              (filling, 'cutlet', 100),
                                                              (filling, 'dinosaur', 200),
                                                              (filling, 'sausage', 300),
                                                              ])
    def test_ingredients_return_name_and_price(self, ingridient_type, name, price):
        ingredient = Ingredient(ingridient_type, name, price)
        assert (ingredient.get_type() == ingridient_type and ingredient.get_name() == name
                and ingredient.get_price() == price)
