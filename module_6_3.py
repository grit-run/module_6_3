class Horse:
    sound = "Frrr"

    def __init__(self):
        self.x_distance = 0

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle(Horse):
    sound = "I train, eat, sleep, and repeat"

    def __init__(self):
        super().__init__()
        self.y_distance = 0

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Eagle, Horse):

    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        print(super().fly(dx))
        print(super().run(dy))

    def get_pos(self):
        return super().fly(0), super().run(0)

    def voice(self):
        scream = super().sound
        print(scream)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
