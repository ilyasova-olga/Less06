class Stationery:
    title = 'Stationery'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        super().draw()
        print('\tРисуем ручкой')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        super().draw()
        print('\tРисуем карандашом')


class Handle(Stationery):
    title = 'Маркер'

    def draw(self):
        super().draw()
        print('\tРисуем маркером')


if __name__ == '__main__':
    pen = Pen()
    print(f'Инструмент: {pen.title}')
    pen.draw()

    pencil = Pencil()
    print(f'Инструмент: {pencil.title}')
    pencil.draw()

    handle = Handle()
    print(f'Инструмент: {handle.title}')
    handle.draw()