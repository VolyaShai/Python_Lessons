class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self):
        direction = input("Введите направление:")
        print(f"{self.name} поверхнула {direction}")

    def show_speed(self):
        print(f"{self.name} едет со скоростью {self.speed}")
        if self.is_police == True:
            print(f"Может ехать с любой скростью! Это полицейская машина! ")


class TownCar(Car):
    def show_speed(self):
        print(f"{self.name} едет со скоростью {self.speed}. Это слишком быстро!"
              if self.speed > 60 else super().show_speed())


class WorkCar(Car):
    def show_speed(self):
        print(f"{self.name} едет со скоростью {self.speed}. Это слишком быстро!"
              if self.speed > 40 else super().show_speed())


class SportCar(Car):
    pass


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=True)


town_car = TownCar(80, "green", "Mazda")
work_car = WorkCar(60, "white", "Mercedes")
sport_car = SportCar(100, "red", "Ferrari")
police_car = PoliceCar(60, "white-blue", "Ford")

list_cars = [town_car, work_car, sport_car, police_car]

for car in list_cars:
    car.go()
    car.show_speed()
    car.turn()
    car.stop()
