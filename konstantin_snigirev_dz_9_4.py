# Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def car_info(self):
        info = f'Name: {self.name}, Color: {self.color}, Speed: {self.speed}'
        return info


    def car_start(self):
        start = 'Car started'
        return start


    def car_stoped(self):
        stop = 'Car stopped'
        return stop


    def car_turned(self, direction):
        self.direction = direction
        return f'{self.color} {self.name} turned {self.direction}'


    def show_speed(self):
        print(f'Current Speed: {self.speed}')


    def check_police(self):
        return f'Police: {self.is_police}'


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


    def show_speed(self):
        print(f'Speed: {self.speed}') if self.speed <= 60 else print('Overspeeding')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


    def show_speed(self):
        print(f'Speed: {self.speed}') if self.speed <= 40 else print('Overspeeding')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)



car_1 = TownCar(100, 'Red', 'Mazda', )
print(car_1.car_start())
print(car_1.car_info(), car_1.show_speed())
print(car_1.check_police())
print(car_1.car_turned('Right'))
print(car_1.car_stoped())


