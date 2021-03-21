# 4. Реализуйте базовый класс Car.
# - у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# - опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# - добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# - для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name}: {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name}: {self.speed} км/ч')
        if self.speed > 60:
            print(f'Скорость городского автомобиля {self.name} должна быть не выше 60 км/ч. Снижайте скорость!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name}: {self.speed} км/ч')
        if self.speed > 40:
            print(f'Скорость рабочего автомобиля {self.name} должна быть не выше 40 км/ч. Снижайте скорость!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


ferrari = SportCar(180, 'белый', 'Ferrari', False)
print(ferrari.name)
print(f'{4 * " "}цвет {ferrari.name}: {ferrari.color}')
print(f'{4 * " "}скорость {ferrari.name}: {ferrari.speed} км/ч')
print(f'{4 * " "}{ferrari.name} - полицейская машина') if ferrari.is_police else \
    print(f'{4 * " "}{ferrari.name} - не полицейская машина')
ferrari.go()
ferrari.turn('налево')
ferrari.show_speed()
ferrari.stop()

hyundai = TownCar(70, 'коричневый', 'Hyundai', False)
print(hyundai.name)
print(f'{4 * " "}цвет {hyundai.name}: {hyundai.color}')
print(f'{4 * " "}скорость {hyundai.name}: {hyundai.speed} км/ч')
print(f'{4 * " "}{hyundai.name} - полицейская машина') if hyundai.is_police else \
    print(f'{4 * " "}{hyundai.name} - не полицейская машина')
hyundai.go()
hyundai.turn('направо')
hyundai.show_speed()
hyundai.speed = 59
print(f'{4 * " "}скорость {hyundai.name}: {hyundai.speed} км/ч')
hyundai.show_speed()
hyundai.stop()

ford = WorkCar(55, 'синий', 'Ford', False)
print(ford.name)
print(f'{4 * " "}цвет {ford.name}: {ford.color}')
print(f'{4 * " "}скорость {ford.name}: {ford.speed} км/ч')
print(f'{4 * " "}{ford.name} - полицейская машина') if ford.is_police else \
    print(f'{4 * " "}{ford.name} - не полицейская машина')
ford.go()
ford.turn('направо')
ford.show_speed()
ford.speed = 39
print(f'{4 * " "}скорость {ford.name}: {ford.speed} км/ч')
ford.show_speed()
ford.stop()

bmw = PoliceCar(90, 'черный', 'BMW', True)
print(bmw.name)
print(f'{4 * " "}цвет {bmw.name}: {bmw.color}')
print(f'{4 * " "}скорость {bmw.name}: {bmw.speed} км/ч')
print(f'{4 * " "}{bmw.name} - полицейская машина') if bmw.is_police else \
    print(f'{4 * " "}{bmw.name} - не полицейская машина')
bmw.go()
bmw.turn('налево')
bmw.show_speed()
bmw.stop()
