from abc import ABC, abstractmethod


class Clothes(ABC):
    all_cons = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def tissue_cons(self):
        pass

    def __add__(self, other):
        Clothes.all_cons += self.tissue_cons + other.tissue_cons
        return round(Clothes.all_cons, 3)


class Coat(Clothes):
    @property
    def tissue_cons(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):
    @property
    def tissue_cons(self):
        return self.param * 2 + 0.3


coat = Coat(float(40))
suit = Suit(1.65)
print(f"Вам потребуется {coat + suit} метров ткани")
