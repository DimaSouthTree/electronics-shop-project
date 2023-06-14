import pytest

from src.phone import Phone
from src.item import Item

phone1 = Phone("iPhone 14", 120_000, 5, 2)
phone2 = Item("iPhone 13", 100000, 15)


def test__init__():
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2

def test__add__():
    assert phone2 + phone1 == 20
    assert phone1 + phone2 == 20

def test__repr__():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"