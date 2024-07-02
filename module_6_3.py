class Horse:

    def __init__(self):
        self.x_distance = 0
        self.sound = "Frrr"

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle(Horse):
    def __init__(self):
        super().__init__()
        self.y_distance = 0
        self.sound = "I train, eat, sleep, and repeat"

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Eagle, Horse):

    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx),
        self.fly(dy)

    def get_pos(self):
        return self.run(0), self.fly(0)

    def voice(self):
        print(self.sound)


if __name__ == '__main__':
    p1 = Pegasus()
    print(p1.get_pos())
    p1.move(10, 15)
    print(p1.get_pos())
    p1.move(-5, 20)
    print(p1.get_pos())
    p1.voice()
#    print(Pegasus.__mro__)
#    print(p1.__dir__())
