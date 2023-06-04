"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

test_1 = Item("Test_1", 10000, 10)
test_2 = Item("Test_2", 10000, 0)
def test_calculate_total_price():
    assert test_1.calculate_total_price() == 100000
    assert test_2.calculate_total_price() == 0

def test_apply_discount():
    ...