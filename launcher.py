import random
import pgzrun

HEIGHT = 600
WIDTH = 800
circlerad = 20
objs = []
targets = []


import random

targets = []

class Target:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, HEIGHT - 150)

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), 20, "red")


def add_Target():
    if len(targets) < 5:
        targets.append(Target())


clock.schedule_interval(add_Target, 5.0)


class bullett:
    def __init__(self,bulletposx,bullettposy):
        self.bulletposx = bulletposx
        self.bulletposy = bullettposy
        self.velocity = 2

    def update(self):
        self.bulletposx = self.bulletposx + self.velocity
        if self.bulletposx > WIDTH + circlerad:
            objs.remove(self)

    def draw(self):
        screen.draw.filled_circle((self.bulletposx,self.bulletposy),circlerad,(255,255,255))

def add_bullett():
    if len(objs) > 1:
        try:
            for x in range(len(objs)):
                objs[x].update()
        except:
            pass

def on_mouse_down(pos):
    bulletposx = pos[0]
    bulletposy = pos[1]
    objs.append(bullett(bulletposx,bulletposy))

def draw():
    screen.clear()
    if len(objs) > 1:
        try:
            for x in range(len(objs)):
                objs[x].draw()
        except:
            pass
    if len(targets) > 1:
        try:
            for x in range(len(targets)):
                targets[x].draw()
        except:
            pass

def update():
    add_bullett()
    add_Target()
    draw()

pgzrun.go()
pgzrun.go()
