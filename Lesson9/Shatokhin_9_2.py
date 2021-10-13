class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self, mass=1, thickness=1):
        return self._width * self._length * mass * thickness


my_road = Road(22, 33)
print(my_road.get_mass(10, 15))
