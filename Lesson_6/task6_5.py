class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки")


class Pen (Stationery):
    def draw(self):
        print(f"Тут мы рисуем {self.title} ручкой")


class Pencil (Stationery):
    def draw(self):
        print(f"Тут уже рисуем {self.title} карандашом")


class Handle (Stationery):
    def draw(self):
        print(f"А тут рисуем {self.title} маркером!")


stationery = Stationery()
pen = Pen("красной")
pencil = Pencil("зеленым")
handle = Handle("желтым")

draw_list = [stationery, pen, pencil, handle]

for el in draw_list:
    el.draw()
