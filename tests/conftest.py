import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_price.return_value = 100
    mock_bun.get_name.return_value = 'black bun'
    return mock_bun

@pytest.fixture
def mock_sauce_ingridient():
    mock_sause = Mock()
    mock_sause.get_price.return_value = 100
    mock_sause.get_name.return_value = 'hot sauce'
    mock_sause.get_type.return_value = 'sauce'
    return mock_sause

@pytest.fixture
def mock_filling_ingridient():
    mock_filling = Mock()
    mock_filling.get_price.return_value = 100
    mock_filling.get_name.return_value = 'cutlet'
    mock_filling.get_type.return_value = 'filling'
    return mock_filling