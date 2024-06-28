class Horse:
    def __init__(self, x_distance=0, sound="Frrr"):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle(Horse):
    def __init__(self, y_distance=0):
        self.y_distance = y_distance
        super().__init__()
        self.sound = "I train, eat, sleep, and repeat"

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Eagle, Horse):

    def __init__(self, x_distance=0, y_distance=0, sound=""):
   #    Eagle.__init__(self, y_distance, sound)
   #    Horse.__init__(self, x_distance, sound)
        super().__init__()


    def move(self, dx, dy):
        print(super().fly(dx))
        print(super().run(dy))

    def get_pos(self):
        return super().fly(0), super().run(0)

    def voice(self):
        print(super().sound)



p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
