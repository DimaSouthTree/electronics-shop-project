from csv import DictReader


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0

    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """инициализирует экземпляры класса `Item` данными из файла _src/items.csv_"""
        fail_items_handel = open('../src/items.csv', 'r')
        items_csv_reader = DictReader(fail_items_handel)

        for row in items_csv_reader:
            name = row.get("name")
            price = int(row.get("price"))
            quantity = int(row.get("quantity"))
            Item.all.append(Item(name, price, quantity))

    @staticmethod
    def string_to_number(str_int):
        """статический метод, возвращающий число из числа-строки"""
        if "." in str_int:
            return int(str_int[0])
        else:
            return int(str_int)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        """проверяет, что длина наименования товара не больше 10 симвовов"""
        if len(new_name) <= 10:
            self.__name = new_name
            return self.__name
        else:
            raise Exception: Длина наименования товара превышает 10 символов.
            # print("Exception: Длина наименования товара превышает 10 символов.")
