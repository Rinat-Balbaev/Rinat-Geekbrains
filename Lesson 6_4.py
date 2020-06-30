class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} is going'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turning right'

    def turn_left(self):
        return f'{self.name} is turning left'

    def show_speed(self):
        return f'Current speed of {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than speed limit for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of WorkCar {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than speed limit for work cars'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is a police car'
        else:
            return f'{self.name} is not a police car'


car_subaru = SportCar(120, 'Red', 'Subaru', False)
car_landcruiser = TownCar(70, 'Silver', 'Land Cruiser', False)
car_gazel = WorkCar(70, 'White', 'Gazel', True)
car_police = PoliceCar(110, 'Police',  'Police', True)
print(car_subaru.turn_right())
print(f'{car_subaru.name} is travelling at speed {car_subaru.speed} km/h')
print(car_police.police())
print(f'{car_landcruiser.name} is travelling at speed {car_landcruiser.speed} km/h. {car_landcruiser.show_speed()}')
