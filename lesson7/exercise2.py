from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def get_fabric(self):
        pass


class Coat(Clothes):

    def __init__(self, V):
        self.V = V

    @property
    def get_fabric(self):
        return round(self.V/6.5 + 0.5, 2)


class Costume(Clothes):

    def __init__(self, H):
        self.H = H

    @property
    def get_fabric(self):
        return 2*self.H + 0.3


coat = Coat(10)
costume = Costume(6)
print(f"Расход ткани на пальто: {coat.get_fabric}")
print(f"Расход ткани на костюм: {costume.get_fabric}")
print(f"Общий расход ткани: {coat.get_fabric + costume.get_fabric}")
