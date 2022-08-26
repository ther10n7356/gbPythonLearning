class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        print(f"{self.name} повернула на {direction}")

    def show_speed(self):
        print(f"Скорость {self.name} {self.speed}")


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"Машина {self.name} превысила скорость")


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"Машина {self.name} превысила скорость")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(65, "White", "Volvo", False)
print(f"Имя машины: {town_car.name}")
print(f"Скорость машины: {town_car.speed}")
print(f"Цвет машины: {town_car.color}")
print(f"Полицеская машина: {town_car.is_police}")
town_car.go()
town_car.turn("налево")
town_car.show_speed()
town_car.stop()

sport_car = SportCar(100, "Blue", "Ferrari", False)
print(f"Имя машины: {sport_car.name}")
print(f"Скорость машины: {sport_car.speed}")
print(f"Цвет машины: {sport_car.color}")
print(f"Полицеская машина: {sport_car.is_police}")
sport_car.go()
sport_car.turn("налево")
sport_car.show_speed()
sport_car.stop()

work_car = WorkCar(65, "Black", "Лада", False)
print(f"Имя машины: {work_car.name}")
print(f"Скорость машины: {work_car.speed}")
print(f"Цвет машины: {work_car.color}")
print(f"Полицеская машина: {work_car.is_police}")
work_car.go()
work_car.turn("налево")
work_car.show_speed()
work_car.stop()

police_car = PoliceCar(80, "Yellow", "Mercedes", True)
print(f"Имя машины: {police_car.name}")
print(f"Скорость машины: {police_car.speed}")
print(f"Цвет машины: {police_car.color}")
print(f"Полицеская машина: {police_car.is_police}")
police_car.go()
police_car.turn("налево")
police_car.show_speed()
police_car.stop()
