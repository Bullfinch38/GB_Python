# . Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    _length, _width = 0, 0


    def __init__(self, length, width, weight, thickness):
        self._weight, self._thickness, self._lenght, self._width = weight / 1000, thickness, length, width

    def asplhalt(self):
        return self._lenght * self._width * self._weight * self._thickness

calc = Road(5000, 20, 25, 5)
print(calc.asplhalt())


#############################

class Road:
    def __init__(self, length, width):
        self._lenght = length
        self._width = width

    def count_mass(self, layer):
        print(f'Asphalt weight {int((layer * self._lenght * self._width * 25) / 1000)} tons')

road = Road(5000, 20)
road.count_mass(5)