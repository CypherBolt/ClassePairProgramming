import random
import pgzrun
import time

from pygame.draw import rect

HEIGHT = 600
WIDTH = 800
circlerad = 20
objs = []
targets = []
score = 0

class Target:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, int(HEIGHT - 300))

    def draw(self):
        screen.draw.filled_circle((self.x,self.y),circlerad,"red")

    def pos(self):
        return self.x, self.y

    def remove(self):
        targets.remove(self)

def add_Target():
    if len(targets) < 10:
        targets.append(Target())

clock.schedule_interval(add_Target, 5.0)

class bullett:
    def __init__(self,bulletposx,bullettposy):
        self.bulletposx = bulletposx
        self.bulletposy = bullettposy
        self.velocity = 10

    def update(self):
        if not self.bulletposy < 0 - circlerad:
            self.bulletposy = self.bulletposy - self.velocity
        else:
            objs.remove(self)

    def pos(self):
        return self.bulletposx, self.bulletposy

    def draw(self):
        screen.draw.filled_circle((self.bulletposx,self.bulletposy),circlerad,(255,255,255))


def add_bullett():
    if len(objs) > 1:
        try:
            for x in range(len(objs)):
                objs[x].update()
        except:
            pass

def bullethit():
    global score
    try:
        for x in range(len(objs)):
            x1 = objs[x].pos()[0]
            y1 = objs[x].pos()[1]
            x2 = targets[x].pos()[0]
            y2 = targets[x].pos()[1]
            if ((x2-x1)**2 + (y2-y1)**2)**0.5 < 40:
                score += 1
                targets[x].remove()
    except:
        pass

def on_mouse_down(pos):
    bulletposx = pos[0]
    bulletposy = pos[1]
    objs.insert(0, bullett(bulletposx,bulletposy))

def draw():
    screen.clear()
    try:
        for x in range(len(objs)):
            objs[x].draw()
    except:
        pass
    try:
        for x in range(len(targets)):
            targets[x].draw()
    except:
        pass
    screen.draw.text((str(score)), (10, 10))

def update():
    time.sleep(0.001)
    add_bullett()
    add_Target()
    bullethit()
    draw()

pgzrun.go()