"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

test_1 = Item("Test_1", 10000, 10)
test_2 = Item("Test_2", 10000, 0)


def test_calculate_total_price():
    assert test_1.calculate_total_price() == 100000
    assert test_2.calculate_total_price() == 0


Item.pay_rate = 0.8
# применяем скидку
test_2.apply_discount()


def test_apply_discount():
    assert test_1.price == 10000
    assert test_2.price == 8000


def test_name():
    assert test_1.name == "Test_1"
    assert test_2.name == "Test_2"

    test_1.name = "Test_3"
    assert test_1.name == "Test_3"


def test__repr__():
    repr(test_1) == "Item('Test_1', 10000, 10)"


def test__srt__():
    str(test_1) == print(test_1.name)
