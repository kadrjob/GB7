class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Stationery named {self.title} draw!')


class Pen(Stationery):
    def draw(self):
        print(f'Pen named {self.title} draw!')


class Pencil(Stationery):
    def draw(self):
        print(f'Pencil named {self.title} draw!')


class Handle(Stationery):
    def draw(self):
        print(f'Handle named {self.title} draw!')


my_stat = Stationery('Stationery')
my_stat.draw()

my_pen = Pen('Pen')
my_pen.draw()

my_pencil = Pencil('Pencil')
my_pencil.draw()

my_handle = Handle('Handle')
my_handle.draw()
