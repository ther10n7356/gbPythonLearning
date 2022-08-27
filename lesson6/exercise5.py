class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print("Рисуем карандашом")


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print("Рисуем ручкой")


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print("Рисуем маркером")


pen = Pen("Ручка")
pen.draw()
pencil = Pencil("Карадаш")
pencil.draw()
handle = Handle("Маркер")
handle.draw()
