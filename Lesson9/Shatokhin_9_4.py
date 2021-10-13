class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, name='BMW', color='Black', speed=0, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'{self.name} run')

    def stop(self):
        print(f'{self.name} stop')

    def turn(self, direction):
        print(f'{self.name} turn {direction}')

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')

    def get_name(self):
        return self.name


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name='BMW', color='Black', speed=0, is_police=True):
        super().__init__(name, color, speed, is_police)
        self.is_police = is_police


town_car = TownCar('LADA', 'White', 30)
print(f'Car name: {town_car.get_name()} color: {town_car.color} speed: {town_car.speed}')
town_car.turn('LEFT')
print(f'Car name: {town_car.get_name()} speed {town_car.speed} is police: {town_car.is_police}')

police_car = PoliceCar('MB', 'Yellow', 80)
print(f'Car name: {police_car.get_name()} color: {police_car.color} speed: {police_car.speed}')
police_car.turn('RIGHT')
print(f'Car name: {police_car.get_name()} speed {police_car.speed} is police: {police_car.is_police}')