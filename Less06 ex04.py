class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f' {self.name} тронулся.'

    def stop(self):
        return f'\n {self.name} остановился.'

    def turn(self, direction):
        return f'\n {self.name} повернул {direction}'

    def show_speed(self):
        return f'\nСкорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        # def __init__(self, speed, color, name, is_police):
        #     super().__init__(speed, color, name, is_police)
        if self.speed > 60:
            return f'\nСкорость выше разрешенной! Скорость {self.speed}'
        else:
            return f'Скорость {self.name} не превышена'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nСкорость выше разрешенной! Скорость {self.speed}'
        else:
            return f'Скорость {self.name} не превышена'


class PoliceCar(Car):
    pass


town = TownCar('Мерседес', 70, 'синий', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('влево'), town.turn('вправо'), town.stop())

sport = SportCar('Феррари', 170, 'красный', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('влево'), sport.stop())

work = WorkCar('Газель', 60, 'зеленый', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('вправо'), work.stop())

police = PoliceCar('Полиция', 100, 'бело-синий', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('вправо'), work.stop())