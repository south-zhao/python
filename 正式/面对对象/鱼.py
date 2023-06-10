import random as r


class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
        print("我的位置：", self.x, self.y)


class Carp(Fish):
    pass


class Sal(Fish):
    pass


class Gold(Fish):
    pass


class Shark(Fish):
    def __init__(self):
        Fish.__init__(self)
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("eat")
            self.hungry = False
        else:
            print("full")


fish = Fish()
fish.move()
gold = Gold()
gold.move()
sal = Sal()
sal.move()
sal.move()
shark = Shark()
shark.eat()
shark.eat()
shark.move()
