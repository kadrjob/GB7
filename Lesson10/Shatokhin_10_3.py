class Cell:

    def __init__(self, nucleus_count):
        self.nucleus_count = nucleus_count

    def __add__(self, other):
        return Cell(self.nucleus_count + other.nucleus_count)

    def __sub__(self, other):
        if (self.nucleus_count - other.nucleus_count) > 0:
            return Cell(self.nucleus_count - other.nucleus_count)
        else:
            print(f'Ошибка вычитания клеток!')

    def __mul__(self, other):
        return Cell(self.nucleus_count * other.nucleus_count)

    def __floordiv__(self, other):
        return Cell(self.nucleus_count / other.nucleus_count)

    def __truediv__(self, other):
        return Cell(self.nucleus_count // other.nucleus_count)

    def make_order(self, nucleus_in_row):
        str_cell = ''
        for i in range(1, (self.nucleus_count // nucleus_in_row) + 1):
            str_cell = str_cell + '*' * nucleus_in_row + '\n'

        if (self.nucleus_count % nucleus_in_row) > 0:
            str_cell = str_cell + ('*' * (self.nucleus_count % nucleus_in_row) + '\n')

        return str_cell


c1 = Cell(5)
c2 = Cell(2)

print('add')
c3 = c1 + c2
print(c3.nucleus_count)

print('sub')
c3 = c1 - c2
print(c3.nucleus_count)

print('mul')
c3 = c1 * c2
print(c3.nucleus_count)

print('__floordiv__')
c3 = c1 / c2
print(c3.nucleus_count)

print('__truediv__')
c3 = c1 // c2
print(c3.nucleus_count)

print()
print(c1.make_order(3))
