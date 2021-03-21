# 5. Реализовать класс Stationery (канцелярская принадлежность).
# - определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# - создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# - в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить
# уникальное сообщение;
# - создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationary:

    def __init__(self, title):
        self.title = title
        self._output_text = 'Запуск отрисовки'

    def draw(self):
        print(self._output_text)


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}. {self._output_text}')


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}. {self._output_text}')


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}. {self._output_text}')


stationary_all = Stationary('Вся канцелярская принадлежность')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
stationary_all.draw()
pen.draw()
pencil.draw()
handle.draw()
