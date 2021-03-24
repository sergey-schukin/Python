# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта —  одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
# пальто и костюм. У этих типов одежды существуют параметры: размер (для  пальто) и рост (для костюма).
# Это могут быть обычные числа:  V и H , соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма  (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора  @property .


from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @property
    @abstractmethod
    def fabric_required(self):
        pass

    @property
    @abstractmethod
    def measuring(self):
        pass

    @abstractmethod
    def _calc_fabric_required(self):
        pass


class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, name, measuring):
        self.name = name
        self._measuring = measuring
        self._fabric_required = None

        self._clothes.append(self)

    def _calc_fabric_required(self):
        raise NotImplemented

    @property
    def fabric_required(self):
        if not self._fabric_required:
            self._calc_fabric_required()

        return self._fabric_required

    @property
    def measuring(self):
        return self._measuring

    @measuring.setter
    def measuring(self, measuring):
        self._measuring = measuring
        self._fabric_required = None

    @property
    def total_fabric_required(self):
        return f'Для пошива пальто и костюма ' \
               f'требуется {sum([item.fabric_required for item in self._clothes])} кв. метров ткани'


class Coat(Clothes):
    def _calc_fabric_required(self):
        self._fabric_required = self.measuring / 6.5 + 0.5

    @property
    def V(self):
        return self.measuring

    @V.setter
    def V(self, size):
        self.measuring = size

    def __str__(self):
        return f"Для пошива пальто {self.measuring} размера " \
               f"требуется {self.fabric_required} кв. метров ткани"


class Suit(Clothes):
    def _calc_fabric_required(self):
        self._fabric_required = 2 * self.measuring / 100 + 0.3

    @property
    def H(self):
        return self.measuring

    @H.setter
    def H(self, height):
        self.measuring = height

    def __str__(self):
        return f"Для пошива костюма на рост {self.measuring} см. " \
               f"требуется {self.fabric_required} кв. метров ткани"


if __name__ == '__main__':
    coat = Coat('Пальто', 48)
    print(coat)
    coat.V = 52
    print(coat)

    suit = Suit('Костюм', 181)
    print(suit)
    suit.H = 200
    print(suit)

    print(coat.total_fabric_required)
    print(suit.total_fabric_required)
