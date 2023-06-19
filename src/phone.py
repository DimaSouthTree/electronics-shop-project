from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        # super().__repr__()
        return f'{self.__class__.__name__}' + f"('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __add__(self, other):
        if not isinstance(other, (Phone, Item)):
            raise ArithmeticError("Правый аргумент должен принадлежать Phone или Item")

        return self.quantity + other.quantity

    def __radd__(self, other):
        return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        if isinstance(new_number_of_sim, int):
            if new_number_of_sim > 0:
                self.__number_of_sim = new_number_of_sim
                return self.__number_of_sim
            else:
                raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
