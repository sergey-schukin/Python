# 2. Реализовать класс Road (дорога).
# - определить атрибуты: length (длина), width (ширина);
# - значения атрибутов должны передаваться при создании экземпляра класса;
# - атрибуты сделать защищёнными;
# - определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# - использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# - проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_consumption(self, weight_kg_per_cm, depth_cm):
        asphalt_total_weight = self._length * self._width * weight_kg_per_cm * depth_cm / 1000
        print(f'Для укладки асфальта весом {weight_kg_per_cm}кг/см толщиной {depth_cm}см на дорогу '
              f'длиной {self._length}м и шириной {self._width}м требуется {asphalt_total_weight} тонн асфальта')


south_road = Road(5000, 20)
south_road.asphalt_consumption(25, 5)
