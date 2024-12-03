from praktikum.burger import Burger


class DefaultBurgerData():
    burger_price = 400
    receipt_text = ('(==== black bun ====)\n'
                    '= sauce hot sauce =\n'
                    '= filling cutlet =\n'
                    '(==== black bun ====)\n'
                    '\n'
                    'Price: 400')

    @staticmethod
    def create_defailt_burger(mock_bun, mock_sauce_ingridient, mock_filling_ingridient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce_ingridient)
        burger.add_ingredient(mock_filling_ingridient)
        return burger
