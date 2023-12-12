class Engine:

    def __init__(self, power: int, company: str):
        self.power = power
        self.company = company


class Driver:

    def __init__(self, experience: int, name: str, surname: str):
        self.experience = experience
        self.name = name
        self.surname = surname


class Person(Driver):

    def get_person(self, age: int):
        self.age = age


class Car:

    def __init__(self, car_brand: str, car_class: str, car_weight: int, car_driver: Driver, car_engine: Engine):
        self.car_brand = car_brand
        self.car_class = car_class
        self.car_weight = car_weight
        self.car_driver = car_driver
        self.car_engine = car_engine

    def start(self) -> None:
        print('Поехали')

    def stop(self) -> None:
        print('Останавливаемся')

    def turnRight(self) -> None:
        print('Поворот направо')

    def turnLeft(self) -> None:
        print('Поворот налево')

    def toString(self, ) -> None:
        print()


class Lorry(Car):

    def get_truck(self, truck_weight: int) -> None:
        self.truck_weight = truck_weight


class SportCar(Car):

    def get_sport_car(self, sport_car_speed: int):
        self.sport_car_speed = sport_car_speed


print('Hello')
engine = Engine(1000, 'Toyota')
print(engine)
print('What')
