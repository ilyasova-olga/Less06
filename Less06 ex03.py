class Worker:

    name = str()
    surname = str()
    position = str()
    _income = {'wage': None, 'bonus': None}

    def __init__(self, name, surname, position, wage, bonus):

        self.position = position
        self.name = name
        self.surname = surname
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):

    def get_full_name(self):

        return f'{self.name} {self.surname}'

    def get_total_income(self):

        return sum(self._income.values())

    def get_position(self):
        return {self.position()}




if __name__ == '__main__':
    pos = Position('Olga', 'Ilyasova', 'analyst', 180000, 20000)

    print(pos.get_full_name())
    print(pos.get_total_income())
    print(pos.position)