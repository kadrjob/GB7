class Worker:
    name = ''
    surname = ''
    position = ''
    __income = {'wage': 0, 'bonus': 0}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self, wage, bonus):
        self._Worker__income['wage'] = wage
        self._Worker__income['bonus'] = bonus
        return sum(self._Worker__income.values())


my_pos = Position()
my_pos.name = 'Ivan'
my_pos.surname = 'Ivanov'

print(my_pos.get_full_name())
print(my_pos.get_total_income(100, 50))
