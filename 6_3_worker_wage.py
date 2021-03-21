# 3. Реализовать базовый класс Worker (работник).
# - определить атрибуты: name, surname, position (должность), income (доход);
# - последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# - создать класс Position (должность) на базе класса Worker;
# - в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# - проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход с учетом премии составляет: {self._income["wage"] + self._income["bonus"]}'


worker_1 = Position('John', 'Smith', 'mechanic', 20000, 2000)
worker_2 = Position('Brian', 'Brown', 'taxi driver', 15000, 5000)
print(worker_1.get_full_name())
print(f'Позиция: {worker_1.position}')
print(worker_1.get_total_income())
print(worker_2.get_full_name())
print(f'Позиция: {worker_2.position}')
print(worker_2.get_total_income())
